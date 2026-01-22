import logging
import os
from datetime import datetime

LOG_FILE = datetime.now().strftime("%Y-%m-%d_%H_%M_%S") + ".log"


logs_dir=os.path.join(os.getcwd(),'logs')
os.makedirs(logs_dir,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_dir,LOG_FILE)
log_format = "[ %(asctime)s ] %(lineno)s %(name)s - %(levelname)s - %(message)s"

logging.basicConfig(
    filename=LOG_FILE_PATH, 
    format=log_format,  
    level=logging.INFO)

# create a logger object
logger=logging.getLogger("my_logger")
