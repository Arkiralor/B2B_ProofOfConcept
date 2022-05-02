from json import loads, dumps
from os import sep

class FileIO:

    @classmethod
    def write_to_json(cls, data: dict, file_name: str, dir:str):
        with open(f"{dir}{sep}{file_name}.json", "w+t", encoding="utf-8") as data_file:
            data = dumps(data, indent=4)
            data_file.write(data)

    @classmethod
    def write_json_from_string(cls, data:str, file_name: str, dir: str):
        data_dict = loads(data)
        with open(f"{dir}{sep}{file_name}.json", "w+t", encoding="utf-8") as data_file:
            data = dumps(data_dict, indent=4)
            data_file.write(data)

    @classmethod
    def read_from_json(cls, file_name: str, dir:str):
        with open(f"{dir}{sep}{file_name}", "rt", encoding="utf-8") as data_file:
            file_data = data_file.read()
        data_dict = loads(file_data)
        return data_dict

    @classmethod
    def write_to_xml(cls, data: any, file_name: str, dir:str):
        with open(f"{dir}{sep}{file_name}.xml", "w+t", encoding="utf-8") as data_file:
            data_file.write(data)