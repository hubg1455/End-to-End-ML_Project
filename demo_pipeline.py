import logging
import sys
from price_prediction.pipeline.pipeline import Pipeline
from price_prediction.exception import PriceException
from price_prediction.config.configuration import Price_Configuration
from price_prediction.component.data_transformation import DataTransformation

def main():

    try:

        pipeline=Pipeline()
        pipeline.run_pipeline()
        #data_validation_config=Price_Configuration().get_data_transformation_config()
        #print(data_validation_config)
        #schema_file_path =r"E:\FSDS Training\End-to-End-ML_Project\config\schema.yaml"
        #file_path=r"E:\FSDS Training\End-to-End-ML_Project\price_prediction\artifact\data_ingestion\2022-09-18-13-03-50\ingested_data\train\housing.csv"
        #df=DataTransformation.load_data(file_path=file_path,schema_file_path=schema_file_path)
        #print(df.columns)
        #print(df.dtypes)

    except Exception as e:
        logging.error("{e}")
        print(e)
        


if __name__=="__main__":
    main()