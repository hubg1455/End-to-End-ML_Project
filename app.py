
from flask import Flask
from price_prediction.logger import logging
from price_prediction.exception import PriceException
import sys

from price_prediction.exception import PriceException

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])

def index():

    try:
        raise Exception("testing exception")

    except Exception as e:
        price=PriceException(e,sys)
        logging.info(price.error_message)
        logging.info("Testing logging module")
    return "Starting Machine Learning Project"

if __name__=='__main__':
    app.run(debug=True)