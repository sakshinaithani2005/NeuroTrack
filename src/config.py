import os

class Config:

    # Logger Configs
    LOG_DIR: str = os.getenv("LOG_DIR", "logs")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "DEBUG")
    MAX_BYTES: int = int(os.getenv("LOG_MAX_BYTES", 5 * 1024 * 1024))  # 5 MB
    BACKUP_COUNT: int = int(os.getenv("LOG_BACKUP_COUNT", 3))

    # Data Dir (Used in various Configs)
    DATA_DIR: str = os.getenv("DATA_DIR", "Data")
    RAW_DATA:str=os.getenv("RAW_DATA","Data\\RAW_DATA.csv")

    #Mongo db atlas configs
    MONGO_DBNAME: str = os.getenv("MONGO_DBNAME", "brainStroke")
    MONGO_COLLECTION:str=os.getenv("MONGO_COLLECTION", "bp")

