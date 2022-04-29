from os import sep
from apis.api import LinkedInAPI

def main():
    ## For profile parser:
    # with open(f"data_store{sep}uids.csv", "rt", encoding="utf-8") as data:
    #     uid_list = data.read().split("\n")

    # uid_list.sort()

    # for uid in uid_list:
    #     LinkedInAPI.get_profile_details(uid)

    ## For search results:
    LinkedInAPI.get_search_results("Python", "CONTENT")

    ## For post comments
    # LinkedInAPI.get_comments("ACoAJXLmXAMBHA6xI27_UiUhOv7gs5ztFxKJ4TQ")

    # LinkedInAPI.get_feed()


if __name__=="__main__":
    main()