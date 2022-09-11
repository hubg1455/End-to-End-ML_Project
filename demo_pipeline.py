import logging
import sys
from price_prediction.pipeline.pipeline import Pipeline
from price_prediction.exception import PriceException

def main():

    try:

        pipeline=Pipeline()
        pipeline.run_pipeline()

    except Exception as e:
        logging.error("{e}")
        print(e)
        


if __name__=="__main__":
    main()