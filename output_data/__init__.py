'''
Initialising the data directory by generating it
and the log file if they do not exist already.
'''

import os

if not os.path.exists('data'):
    os.makedirs('data')

# if not os.path.exists(f"data{os.sep}data.jso"):
#     with open(f"log{os.sep}sys_logger.log", "w+t", encoding="utf-8")as log_file:
#         log_file.write("")