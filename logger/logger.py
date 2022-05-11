import logging
from os import sep

logging.basicConfig(
    level=logging.INFO,
    handlers=[
            logging.FileHandler(f"log{sep}sys_logger.log"),
            logging.StreamHandler(),
        ]
    )