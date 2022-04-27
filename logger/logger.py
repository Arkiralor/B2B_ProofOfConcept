import logging
from os import sep

logging.basicConfig(
    filename=f"log{sep}sys_logger.log", 
    level=logging.DEBUG
    )