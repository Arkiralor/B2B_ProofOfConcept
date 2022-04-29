
from utils.file_operations import FileIO


## line 233 in linkedin-api.linkedin
FileIO.write_json_from_string(
                data=res._content,
                file_name=f"{params.get('keywords', 'default_search_xml')}_rawSearch",
                dir=f"output_data{os.sep}search_results"
            )