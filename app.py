import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
# from config import pgadim_user, pgadim_pass
import psycopg2


engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/Crash-Dummies-2.0')

connection = engine.connect()




# @app.route("/")
# create classes and write data into db
# pandas insert function <-- revisit if we have time



# @app.route("/queries")
# run queries
# 





# @app.route("/map")
# perform queries and load into map 

# 1. write the data from flask app to the db

#2. transform the data to create plots

