from email import message
import sys,os
from price_prediction.entity.artifact_entity import DataIngestionArtifact
from price_prediction.logger import logging
from price_prediction.exception import PriceException
from price_prediction.entity.config_entity import DataValidationConfig




class DataValidation:

    def __init__(self,data_validation_config:DataValidationConfig,
        data_ingestion_artifact:DataIngestionArtifact):

        try:
            self.data_validation_config=data_validation_config
            self.data_ingestion_artifact=data_ingestion_artifact

        except Exception as e:
            raise PriceException(e,sys) from e

    def is_train_test_file_exists(self) ->bool:
        
        try:

            logging.info("checking if train and test file is available")
            is_train_file_exist=False
            is_test_file_exist=False

            

            train_file_path=self.data_ingestion_artifact.train_file_path
            test_file_path=self.data_ingestion_artifact.test_file_path

            is_train_file_exist=os.path.exists(train_file_path)
            is_test_file_exist=os.path.exists(test_file_path)

            is_available= is_train_file_exist and is_test_file_exist

            logging.info(f"Is my train test file exists?->{is_available}")

            if not is_available:

                training_file=self.data_ingestion_artifact.train_file_path
                testing_file=self.data_ingestion_artifact.test_file_path
                message=f"Training file: {training_file} or Testing file: {testing_file}\
                    is not present"
                logging.info(message)
                raise Exception(message)
                
            return is_available

        except Exception as e:
            raise PriceException(e,sys) from e

    def validate_dataset_schema(self):
        try:
            validation_status=False

            validation_status=True
            return validation_status

        except Exception as e:
            raise PriceException(e,sys) from e



    def initiate_data_validation(self):

        try:
            self.is_train_test_file_exists()
            self.validate_dataset_schema()

            

        except Exception as e:
            raise PriceException(e,sys) from e