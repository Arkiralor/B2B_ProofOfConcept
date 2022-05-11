from os import sep
from apis.api import LinkedInAPI
import json

def main():

    main_api = LinkedInAPI()

    ## For profile parser:
    # with open(f"data_store{sep}uids.csv", "rt", encoding="utf-8") as data:
    #     uid_list = data.read().split("\n")


    # uid_list.sort()

    # for uid in uid_list:
    #     main_api.get_profile_details(uid)

    ## For search results:
    # main_api.search_posts("Python", "CONTENT")

    ## For post comments
    # LinkedInAPI.get_comments("6926503527993204736")

    # main_api.get_feed()

    ## For searching jobs:
    # main_api.get_jobs("python")

    ## Company Details:
    # main_api.get_companies("techvariable")

    ## Search people:
    # main_api.get_people(keywords="python")

    ## Get Python Profile:
    with open("raw_data\search_results\people\python_people.json")as python_people_file:
        python_people_dict = json.load(python_people_file)

    for person in python_people_dict[:10]:
         main_api.get_profile_details(person.get("public_id"))



if __name__=="__main__":
    main()