"""Settings for the database system."""
from decouple import config

DB_ENGINE = config("DB_ENGINE")
DB_USERNAME = config("DB_USERNAME")
DB_PASSWORD = config("DB_PASSWORD")
DB_HOST = config("DB_HOST")
DB_PORT = config("DB_PORT")
DB_NAME = config("DB_NAME")

DB_STRING = "{engine}://{username}:{password}@{host}:{port}/{db_name}".format(
    engine=DB_ENGINE, username=DB_USERNAME, password=DB_PASSWORD,
    host=DB_HOST, port=DB_PORT, db_name=DB_NAME)
