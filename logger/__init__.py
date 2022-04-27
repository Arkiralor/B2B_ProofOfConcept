'''
Initialising the logger by generating the log directory
and the log file if they do not exist already.
'''

import os

if not os.path.exists('log'):
    os.makedirs('log')

if not os.path.exists(f"log{os.sep}sys_logger.log"):
    with open(f"log{os.sep}sys_logger.log", "w+t", encoding="utf-8")as log_file:
        log_file.write("")