import os
import sys
from src.mlproject.exxception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from src.mlproject.utils import read_sql_data
from sklearn.model_selection import train_test_split

from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts','train,csv')
    test_data_path:str=os.path.join('artifacts','test,csv')
    raw_data_path:str=os.path.join('artifacts','raw,csv')



class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    def initiate_data_ingestion(self):
        try:
            df=read_sql_data()
            logging.info("Reading from mysql Database")
            train_data_dir=os.path.dirname(self.ingestion_config.train_data_path )
            os.makedirs(train_data_dir)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            train_set,test_set=train_test_split(df,test_size=.2,random_state=42)
            
            df.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            df.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("Data ingesiton is complete")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)
        

