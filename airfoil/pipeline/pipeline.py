from airfoil.config.configuration import Airfoil_Configuration
from airfoil.logger import logging
from airfoil.exception import AirfoilException

from airfoil.entity.artifact_entity import DataIngestionArtifact
from airfoil.entity.config_entity import DataIngestionConfig
from airfoil.component.data_ingestion import DataIngestion
import os,sys


class Pipeline:

    def __init__(self,config:Airfoil_Configuration=Airfoil_Configuration())->None:
        try:
            self.config=config
        
        except Exception as e:
            raise AirfoilException(e,sys) from e

    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            data_ingestion=DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())

            return data_ingestion.initiate_data_ingestion()
        
        except Exception as e:
            raise AirfoilException(e,sys) from e


    def start_data_validation(self):
        pass

    def start_data_transformation(self):
        pass

    def start_model_trainer_(self):
        pass

    def start_model_evaluation(self):
        pass

    def start_model_pusher_(self):
        pass

    
    def run_pipeline(self):
        try:
            #data_ingestion

            data_ingestion_artifact=self.start_data_ingestion()
        
        except Exception as e:
            raise AirfoilException(e,sys) from e
