from linkedin_api import Linkedin
from os import environ, sep
from dotenv import load_dotenv
from json import loads, dumps
from datetime import datetime

from logger.logger import logging

load_dotenv()


class LinkedInAPI:
    username = environ["LINKEDIN_USERNAME"]
    password = environ["LINKEDIN_PASSWORD"]

    @classmethod
    def get_details(cls, uid: str):   
        detail_dict = {}

        # Authenticate using any Linkedin account credentials
        logging.info(f"[{datetime.now()}]   AUTHENTICATING {cls.username}")
        api = Linkedin(cls.username, cls.password)
        # GET a profile
        logging.info(f"[{datetime.now()}]   GETTING PROFILE INFO for: {uid}")
        profile = api.get_profile(uid)
        detail_dict['profile'] = profile

        # GET a profiles contact info
        logging.info(f"[{datetime.now()}]   GETTING CONTACT INFO for: {uid}")
        contact_info = api.get_profile_contact_info(uid)
        detail_dict['contact_info'] = contact_info

        # GET 1st degree connections of a given profile
        logging.info(f"[{datetime.now()}]   GETTING CONNECTIONS INFO for: {uid}")
        connections = api.get_profile_connections(uid)
        detail_dict['connections'] = connections

        # print(detail_dict)
        with open(f"output_data{sep}{uid}.json", "w+t", encoding="utf-8") as data_file:
            data = dumps(detail_dict, indent=4)
            logging.info(f"[{datetime.now()}]   WRITING PROFILE INFO for: {uid}")
            data_file.write(data)

if __name__=="__main__":
    with open(f"data_store{sep}uids.csv", "rt", encoding="utf-8") as data:
        uid_list = data.read().split("\n")

    for uid in uid_list:
        LinkedInAPI.get_details(uid)

