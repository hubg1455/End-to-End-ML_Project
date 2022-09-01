from airfoil.logger import logging
import sys
from airfoil.entity.config_entity import DataIngestionConfig
from airfoil.exception import AirfoilException


class DataIngestion:

    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            logging.info(f"{'='*20} Data ingestion log started.{'='*20}")
            self.data_ingestion_config=data_ingestion_config

        except Exception as e:
            raise AirfoilException(e,sys) from e


    def initiate_data_ingestion(self)->DataIngestionArtifact:
        try:
            pass

        except Exception as e:
            raise AirfoilException(e,sys) from e
