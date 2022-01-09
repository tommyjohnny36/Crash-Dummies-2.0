from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig


app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)

# Postgres
# URI = "postgresql+psycopg2://postgres:postgres@127.0.0.1/Crash-Dummies-2.0"

