from os import sep
from apis.api import LinkedInAPI

def main():
    ## For profile parser:
    with open(f"data_store{sep}uids.csv", "rt", encoding="utf-8") as data:
        uid_list = data.read().split("\n")

    uid_list.sort()

    for uid in uid_list:
        LinkedInAPI.get_profile_details(uid)

    ## For search results:
    # LinkedInAPI.get_search_results("Python Django", "CONTENT")

    ## For post comments
    # LinkedInAPI.get_comments("6926503527993204736")

    # LinkedInAPI.get_feed()


if __name__=="__main__":
    main()