"""Settings for the database system."""
from dotenv import load_dotenv
import os
load_dotenv()

DB_ENGINE = os.getenv("DB_ENGINE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DB_STRING = "{engine}://{username}:{password}@{host}:{port}/{db_name}".format(
    engine=DB_ENGINE, username=DB_USERNAME, password=DB_PASSWORD,
    host=DB_HOST, port=DB_PORT, db_name=DB_NAME)
