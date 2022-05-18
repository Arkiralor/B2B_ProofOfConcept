from os import sep
from apis.api import LinkedInAPI
import json
from random import randrange, seed
from logger.logger import logging
import argparse
from datetime import datetime

def main():

    main_api = LinkedInAPI()
    ## Search people:
    people = main_api.get_people(keywords="interested in biriyani")
    # print(people)

    with open(f"raw_data{sep}profiles{sep}test.json", "w+t", encoding="utf-8") as data_file:
            data = json.dumps(people, indent=4)
            logging.info(
                f"[{datetime.now()}]   WRITING SEARCH INFO for: 'technical recruiter hiring python'")
            data_file.write(data)



if __name__=="__main__":
    main()