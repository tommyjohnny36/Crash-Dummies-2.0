from sqlalchemy import create_engine, func
import sqlite3
import sqlalchemy as SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Crash-Dummies-2.0.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Passenger = Base.classes.passenger

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)
# migrate = Migrate(app, db)

db = sqlite3.connect('')

@app.route("/")
# create classes and write data into db
# pandas insert function <-- revisit if we have time



@app.route("/queries")
# run queries






@app.route("/map")
# perform queries and load into map 

# 1. write the data from flask app to the db

#2. transform the data to create plots



