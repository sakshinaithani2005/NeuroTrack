from pymongo import MongoClient
from dotenv import load_dotenv
import os
import pandas as pd
from src.config import Config
from src.logger import get_logger

load_dotenv()
logger=get_logger(" Data injestion form mongodb")
def fetch_data_from_mongo():
    try:
        uri = os.getenv("MONGO_URI")
        logger.debug("connected with mongo uri")
        client = MongoClient(uri)
        logger.debug("connected with client")
        db=client[Config.MONGO_DBNAME]
        logger.debug("fetch data from mongo")
        record=db[Config.MONGO_COLLECTION]
        logger.debug("fetch rows")
        data=list(record.find({}))
        logger.debug(f"converting {len(data)} rows of data into list ")
        df = pd.DataFrame(data)
        os.makedirs(Config.DATA_DIR, exist_ok=True)
        df.drop(columns=['_id'],inplace=True)
        df.to_csv(Config.RAW_DATA, index=False)
        logger.debug("converting list into data frame")

        print(df.head())
    except Exception as e:
        logger.error('Unexpected error occurred while loading the data: %s', e)
        raise


if __name__ == "__main__":
    fetch_data_from_mongo()



