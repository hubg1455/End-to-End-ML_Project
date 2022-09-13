import logging
import sys
from price_prediction.pipeline.pipeline import Pipeline
from price_prediction.exception import PriceException
from price_prediction.config.configuration import Price_Configuration

def main():

    try:

        #pipeline=Pipeline()
        #pipeline.run_pipeline()
        data_validation_config=Price_Configuration().get_data_validation_config()
        print(data_validation_config)
        

    except Exception as e:
        logging.error("{e}")
        print(e)
        


if __name__=="__main__":
    main()