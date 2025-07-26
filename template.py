from fileinput import filename
import os
from pathlib import Path   
import logging 


logging.basicConfig(level=logging.INFO,format='[%(asctime)s] :%(message)s: ')



list_of_files = [
    "requirements.txt",
    "setup.py",
    ".env",
    "README.md",
    "main.py",

]


for file in list_of_files:
    file_path= Path(file)
    filedir, file_name = os.path.split(file_path)


    if filedir!="":
        logging.info(f"Creating directory: {filedir} for file: {filename}")
        os.makedirs(filedir,exist_ok=True) #exist_ok=True allows the directory to be created if it does not exist


    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)== 0):
        with open(file_path, 'w') as f:
            pass
            logging.info(f"Creating file: {filename}")
            
            
    else:
        logging.info(f"File already exists: {filename}")

