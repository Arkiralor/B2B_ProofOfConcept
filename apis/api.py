from linkedin_api import Linkedin
from os import environ, sep
from dotenv import load_dotenv
from json import loads, dumps
from datetime import datetime

from logger.logger import logging

load_dotenv()


class LinkedInAPI:

    def __init__(self, username: str = None, password: str = None):
        if username is None or username == "":
            self.username = environ["LINKEDIN_USERNAME"]
        if password is None or password == "":
            self.password = environ["LINKEDIN_PASSWORD"]

        logging.info(f"[{datetime.now()}]   AUTHENTICATING {self.username}")
        self.api = Linkedin(self.username, self.password)

    def get_profile_details(self, uid: str):
        detail_dict = {}

        logging.info(f"[{datetime.now()}]   GETTING PROFILE INFO for: {uid}")
        profile = self.api.get_profile(uid)
        detail_dict['profile'] = profile

        # GET a profiles contact info
        logging.info(f"[{datetime.now()}]   GETTING CONTACT INFO for: {uid}")
        contact_info = self.api.get_profile_contact_info(uid)
        detail_dict['contact_info'] = contact_info

        ## GET 1st degree connections of a given profile
        logging.info(f"[{datetime.now()}]   GETTING CONNECTIONS INFO for: {uid}")
        urn = detail_dict.get('profile', {}).get('entityUrn', "").split(":")[-1]
        connections = self.api.get_profile_connections(urn_id=urn)
        detail_dict['connections'] = connections

        ## GET skills from profile
        skills = self.api.get_profile_skills(uid)
        detail_dict['skills'] = skills

        with open(f"raw_data{sep}profiles{sep}{uid}.json", "w+t", encoding="utf-8") as data_file:
            data = dumps(detail_dict, indent=4)
            logging.info(
                f"[{datetime.now()}]   WRITING PROFILE INFO for: {uid}")
            data_file.write(data)

    def search_posts(self, search_term: str = "Python", search_type: str = "CONTENT"):
        '''
        search_type: ALL|CONTENT|PEOPLE|JOBS|COMPANIES|SCHOOLS|GROUPS|EVENTS|LEARNING|SERVICES|
        '''
        params = {
            "filters": [
                f"resultType->{search_type}"
            ],
            "keywords": search_term,
            "origin": "GLOBAL_SEARCH_HEADER",
        }

        search = self.api.search(
            params=params,
            limit=-1
        )

        with open(f"raw_data{sep}search_results{sep}posts{sep}{search_term.lower()}_{search_type.lower()}.json", "w+t", encoding="utf-8") as data_file:
            data = dumps(search, indent=4)
            logging.info(
                f"[{datetime.now()}]   WRITING SEARCH INFO for: {search_term}")
            data_file.write(data)

    def get_comments(self, post_urn: str, comment_count: int = 100):
        comments = self.api.get_post_comments(post_urn, comment_count)
        with open(f"raw_data{sep}post_comments{sep}{post_urn.lower()}_comments.json", "w+t", encoding="utf-8") as data_file:
            data = dumps(comments, indent=4)
            logging.info(
                f"[{datetime.now()}]   WRITING SEARCH INFO for: {post_urn}")
            data_file.write(data)

    def get_jobs(self, query:str):
        jobs = self.api.search_jobs(query)

        with open(f"raw_data{sep}search_results{sep}jobs{sep}{query}_jobs.json", "w+t", encoding="utf-8") as data_file:
            data = dumps(jobs, indent=4)
            logging.info(f"[{datetime.now()}]   WRITING SEARCH INFO for: {query}")
            data_file.write(data)

    def get_feed(self):
        feed = self.api.get_feed_posts(limit=1000)
        resp = {}
        resp["feed"] = feed
        with open(f"output_data{sep}raw_data{sep}{self.username.lower()}_feed.json", "w+t", encoding="utf-8") as data_file:
            data = dumps(resp, indent=4)
            logging.info(
                f"[{datetime.now()}]   WRITING SEARCH INFO for: {self.username} FEED")
            data_file.write(data)

    def get_companies(self, public_id: str):
        company = self.api.get_company(public_id)

        with open(f"raw_data{sep}companies{sep}{public_id}_company.json", "w+t", encoding="utf-8") as data_file:
            data = dumps(company, indent=4)
            logging.info(f"[{datetime.now()}]   WRITING SEARCH INFO for: {company}")
            data_file.write(data)

    def get_people(
                    self,
                    keywords=None,
                    current_company=None,
                    past_companies=None,
                    regions=None,
                    industries=None,
                    schools=None,
                    profile_languages=None,
                    contact_interests=None,
                    service_categories=None,
                    network_depths=["F", "S", "O"],
                    include_private_profiles=None,
                    keyword_first_name=None,
                    keyword_last_name=None,
                    keyword_title=None,
                    keyword_company=None,
                    keyword_school=None,
                    connection_of=None
                ):
        people = self.api.search_people(
            keywords,
            current_company,
            past_companies,
            regions,
            industries,
            schools,
            profile_languages,
            contact_interests,
            service_categories,
            network_depths,
            include_private_profiles,
            keyword_first_name,
            keyword_last_name,
            keyword_title,
            keyword_company,
            keyword_school,
            connection_of
        )

        with open(f"raw_data{sep}search_results{sep}people{sep}{keywords}_people.json", "w+t", encoding="utf-8") as data_file:
            data = dumps(people, indent=4)
            logging.info(f"[{datetime.now()}]   WRITING SEARCH INFO for: {people}")
            data_file.write(data)




if __name__ == "__main__":
    pass
