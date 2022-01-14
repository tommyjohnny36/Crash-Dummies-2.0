import sqlalchemy as db
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import Column, Date, Integer, Text, create_engine, inspect
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import numpy as np
import json
import pandas as pd



engine = db.create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/Crash-Dummies-2.0')


app = Flask(__name__)

session = Session(bind=engine)

Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()

Accidents = Base.classes.accidents
People = Base.classes.people
Vehicle = Base.classes.vehicle


@app.route("/")
def home():
    return(
        f"Welcome to Crash Dummies 2.0! <br/>"
    
        f"Available Routes:<br/>"

        f"/api/v1.0/vehicles<br/>"
        f" - List of accident information by vehicle type<br/>"

        f"/api/v1.0/age<br/>"
    )
@app.route("/index")
def query():

    df_1 = pd.read_sql('select * from people', 'engine')  

    return df_1.to_json


    session.close()



# @app.route("/queries")
# run queries


# @app.route("/map")
# perform queries and load into map 

# 1. write the data from flask app to the db

#2. transform the data to create plots


if __name__ == '__main__':
    app.run(debug=True)
