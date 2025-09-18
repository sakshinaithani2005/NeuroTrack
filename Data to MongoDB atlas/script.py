from multiprocessing.util import get_logger

from pymongo import MongoClient
from dotenv import load_dotenv
import os
import pandas as pd
from src.logger import get_logger

load_dotenv()
logger=get_logger(" Data injection to mongodb")
def load_data_to_mongo():
    try:
        uri = os.getenv("MONGO_URI")
        client = MongoClient(uri)
        logger.debug('url loaded and connected with mongodb')
        data = pd.read_csv("..\\Data\\brain_stroke.csv")
        logger.debug('csv file  loaded')
        db = client["brainStroke"]
        collection = db["bp"]

        df = data.to_dict("records")
        logger.debug('data converted to json format ')
        collection.insert_many(df)
        logger.info("Data injection to mongodb completed")

    except Exception as e:
        logger.error('Unexpected error occurred while loading the data: %s', e)
        raise

if __name__ == "__main__":
    load_data_to_mongo()
