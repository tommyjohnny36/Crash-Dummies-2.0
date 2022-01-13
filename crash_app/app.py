import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import numpy as np



engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/Crash-Dummies-2.0')


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
def vehicle(state):

    # session = Session(engine)

    """ return all vechicle types  """
    state = session.query.filter_by(state=state).Accidents.state, func.count(Accidents.case_number).\
    group_by(Accidents.state).\
    order_by(func.count(Accidents.case_number).desc()).all()

    return render_template('index.html', state=state)




    session.close()

    state_results = list(np.ravel(state_accidents))

    return jsonify(state_results)


# @app.route("/queries")
# run queries


# @app.route("/map")
# perform queries and load into map 

# 1. write the data from flask app to the db

#2. transform the data to create plots


if __name__ == '__main__':
    app.run(debug=True)
