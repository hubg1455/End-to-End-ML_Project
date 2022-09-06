import logging
import sys
from airfoil.pipeline.pipeline import Pipeline
from airfoil.exception import AirfoilException

def main():

    try:

        pipeline=Pipeline()
        pipeline.run_pipeline()

    except Exception as e:
        logging.error("{e}")
        print(e)
        


if __name__=="__main__":
    main()