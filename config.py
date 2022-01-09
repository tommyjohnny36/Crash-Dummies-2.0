
class DevConfig(Config):
    debug = True
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:postgres@127.0.0.1/Crash-Dummies-2.0"