import pandas as pd
from src.config import Config
from src.logger import get_logger
import os
from sklearn.model_selection import train_test_split


logger=get_logger(" Data splitting")
def load_data():
    """Load data from a CSV file."""
    try:
        df = pd.read_csv(Config.RAW_DATA)
        logger.debug(' raw Data loaded from file')
        return df
    except pd.errors.ParserError as e:
        logger.error('Failed to parse the CSV file: %s', e)
        raise
    except Exception as e:
        logger.error('Unexpected error occurred while loading the data: %s', e)
        raise

def save_data(x_train: pd.DataFrame, x_test: pd.DataFrame, y_train: pd.DataFrame, y_test: pd.DataFrame,data_path: str) -> None:
    """Save the train and test datasets."""
    try:
        raw_data_path = os.path.join(data_path, 'r')
        os.makedirs(raw_data_path, exist_ok=True)
        x_train.to_csv(os.path.join(raw_data_path, "x_train.csv"), index=False)
        x_test.to_csv(os.path.join(raw_data_path, "x_test.csv"), index=False)
        y_train.to_csv(os.path.join(raw_data_path, "y_train.csv"), index=False)
        y_test.to_csv(os.path.join(raw_data_path, "y_test.csv"), index=False)
        logger.debug('Train and test data saved to %s', raw_data_path)
    except Exception as e:
        logger.error('Unexpected error occurred while saving the data: %s', e)
        raise

def main():
    try:
        df=load_data()
        # splitting data into
        train,test=train_test_split(df,test_size=0.2,random_state=42)
        train.to_csv(Config.TRAIN_DATA, index=False)
        test.to_csv(Config.TEST_DATA, index=False)
        logger.info('Train and test data saved to %s', Config.TRAIN_DATA)


    except Exception as e:
        logger.error('Failed to complete the data ingestion process: %s', e)
        print(f"Error: {e}")




if __name__ == '__main__':
    main()