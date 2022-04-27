from src.data.config_reader import *
from src.data.path_finder import *
import pandas as pd
import sqlite3
from sqlite3 import Error
import os


configs = load_config()
def build_tables():
    """Consolidates and write all csv files into a SQLite database
    """

    # Read data path and list all the csv files
    raw_data_path = configs["PATHS"]["RAW"]
    raw_data_path = get_path(raw_data_path)
    data_list = os.listdir(raw_data_path)

    # Access SQLite db
    conn = connect_db()

    # Loop through csv files and insert them as tables
    for file in data_list:
        target_file_path = get_path(raw_data_path, file)
        df = pd.read_csv(target_file_path)
        table_name = file.split(".")[0]
        try:
            df.to_sql(table_name, conn, if_exists="replace", index=False)
        except:
            conn.rollback()
            conn.close()
    conn.close()

def create_db():
    """Creates SQLite Database when called
    """
    agg_data_path = configs["PATHS"]["AGGREGATED"]
    agg_data_path = get_path(agg_data_path)
    db_path = get_path(agg_data_path, "t_db.db")
    if not os.path.exists(db_path):
        _ = sqlite3.connect(db_path)
        print("Database Created as t_db.db!")
    else:
        raise Error("Target db exists")

def connect_db():
    """Manages Database access and returns connection object
    """
    agg_data_path = configs["PATHS"]["AGGREGATED"]
    agg_data_path = get_path(agg_data_path)
    db_path = get_path(agg_data_path, "t_db.db")
    if os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        return conn
    else:
        raise Error("DB does not exist!")

def initiate_database():
    """Main function to handle all operations single-handedly
    """
    try:
        create_db()
    except Error as exc:
        print(exc, " moving on to table building operation...")

    build_tables()
        