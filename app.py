
from flask import Flask
from airfoil.logger import logging
from airfoil.exception import AirfoilException
import sys

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])

def index():

    try:
        raise Exception("testing exception")

    except Exception as e:
        airfoil=AirfoilException(e,sys)
        logging.info(airfoil.error_message)
        logging.info("Testing logging module")
    return "Starting Machine Learning Project"

if __name__=='__main__':
    app.run(debug=True)