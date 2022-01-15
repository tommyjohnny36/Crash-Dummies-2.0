# This Python script connects to a PostgreSQL database and utilizes Pandas to obtain data and create a data frame
# A initialization and configuration file is used to protect the author's login credentials 
import sqlalchemy 
import psycopg2
import pandas as pd
from flask import jsonify
import json
from dbconfig import config



class DBHelper:
# engine = db.create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/Crash-Dummies-2.0')

# session = Session(bind=engine)

# Establish a connection to the database by creating a cursor object
# Obtain the configuration parameters
    def connect(self):
        params = config()
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # Create a new cursor
        return conn

# A function that takes in a PostgreSQL query and outputs a jsonified result
# Store the data as a variable
    def get_data(self):
        connection = self.connect()
        try:
            query = '''SELECT a.case_number, a.month, a.day, a.state, a.city, a.lat, a.lon, p.sex, p.age_label, \
                p.age, p.doa_status, p.vehicle_model, p.vehicle_manufacturer, \
                a.route, a.first_harm, a.man_collision, a.light_condit, a.weather, a.rural_urban, v.hit_run \
                from accidents a \
                inner join people p \
                on a.case_number=p.case_number \
                inner join vehicle v \
                on p.case_number=v.case_number'''

            df = pd.read_sql(query, connection)
            no_dups_df = df.drop_duplicates()
            result = no_dups_df.to_json(orient="records")
            parsed = json.loads(result)
            return (parsed)

        finally:
            # Close the cursor and connection to so the server can allocate
            # bandwidth to other requests
            connection.close()

########################################################
########################################################

    # def get_all_inputs(self):
    #     connection = self.connect()
    #     try:
    #         query = "SELECT description FROM crimes;"
    #         with connection.cursor() as cursor:
    #             cursor.execute(query)
    #         return cursor.fetchall()
    #     finally:
    #         connection.close()

    # def add_input(self, data):
    #     connection = self.connect()
    #     try:
    #         query = "INSERT INTO crimes (description) VALUES (%s);"
    #         with connection.cursor() as cursor:
    #             cursor.execute(query, data)
    #             connection.commit()
    #     finally:
    #         connection.close()

    # def clear_all(self):
    #     connection = self.connect()
    #     try:
    #         query = "DELETE FROM crimes;"
    #         with connection.cursor() as cursor:
    #             cursor.execute(query)
    #             connection.commit()
    #     finally:
    #         connection.close()
