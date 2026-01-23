import os
import json
import sys
from pathlib import Path
import certifi
import pandas as pd
import numpy as np
import pymongo
from networksecurity.logging.logger import logger
from networksecurity.exception.exception import NetworksecurityException
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

load_dotenv()

MONGO_DB_URL = os.getenv('MONGO_DB_URI')
print(MONGO_DB_URL)

class NetworkDataExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworksecurityException(e, sys)
        
    def csv_to_json_converter(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)  
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworksecurityException(e, sys)
    
    def push_json_to_mongodb(self, records: list):
        try:
            myclient = pymongo.MongoClient(
                MONGO_DB_URL,
                tlsCAFile=certifi.where()
            )
    
            myclient.admin.command("ping")
            print("MongoDB connection successful")
            
            my_db = myclient['network']
            my_coll = my_db['network_phising']
            
            result = my_coll.insert_many(records)
            print(f"Successfully inserted {len(result.inserted_ids)} records")
            
            myclient.close()
            
        except Exception as e:
            raise NetworksecurityException(e, sys)

if __name__ == "__main__":
    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json_converter(os.path.join("Network_Data", "phisingData.csv"))
    networkobj.push_json_to_mongodb(records=records)