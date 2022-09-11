import logging
from datetime import datetime
import os


LOG_DIR="airfoil_logs"

CURRENT_TIME_STAMP=f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

LOG_FILE_NAME=f"log_{CURRENT_TIME_STAMP}.logs"

#If there is no directory then need to create directory
os.makedirs(LOG_DIR,exist_ok=True)

#need to create log file path
LOG_FILE_PATH=os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(filename=LOG_FILE_PATH,filemode='w',
format='[%(asctime)s]-%(name)s-%(levelname)s-%(message)s',
level=logging.INFO)