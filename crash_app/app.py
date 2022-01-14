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

con = engine.connect()

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


    query = '''
    SELECT a.case_number, a.state, a.lat, a.lon, p.sex, p.age_label, p.age, p.doa_status, p.vehicle_model, p.vehicle_manufacturer, a.rural_urban, v.hit_run
    from accidents a
    inner join people p
    on a.case_number=p.case_number
    inner join vehicle v
    on p.case_number=v.case_number

'''   

    df = pd.read_sql(query, con=engine)
    no_dups_df = df.drop_duplicates()
    result = no_dups_df.to_json(orient="records")
    parsed = json.loads(result)
    return json.dumps(parsed, indent=4) 



# @app.route("/queries")
# run queries


# @app.route("/map")
# perform queries and load into map 

# 1. write the data from flask app to the db

#2. transform the data to create plots


if __name__ == '__main__':
    app.run(debug=True)
