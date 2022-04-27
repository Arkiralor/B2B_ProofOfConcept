from os import sep
from apis.api import LinkedInAPI

def main():
    with open(f"data_store{sep}uids.csv", "rt", encoding="utf-8") as data:
        uid_list = data.read().split("\n")

    uid_list.sort()

    for uid in uid_list:
        LinkedInAPI.get_profile_details(uid)

if __name__=="__main__":
    main()