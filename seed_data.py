import pandas as pd
import numpy as np
import sqlite3


db = "./database.db" #SQLite database is used for this task, this is document that is easy to use and no installations required

def read_task_data():
    """
    Read task data from the csv file and loads it into a pandas dataframe 

    returns: pandas dataframe
    """
    data = pd.read_csv("data_set/task_data.csv")
    return data

def clean_data(data):
    """
    1. Removes ID column from the dataframe, this column serves no purpose since this 
       only data to save and no need to start from big numbers like those in the csv.
    2. Have the data start at 1, and rename it to id which will be used in the database
       to reflect actual number of records.
    3. Format timestamp column to remove suffix which is the same for all values in the column.
    4. Format duration to remove days suffix, which is the same for all values in the column.
    5. Format temparature for consistency for all values to have the same precision.

    params: data (pandas dataframe)

    returns: pandas dataframe
    """
    data = data.drop(columns=["id"])

    data.index = np.arange(1, len(data)+1)

    data.index.name = "id"

    data["timestamp"] = data["timestamp"].str[:-7]

    data["duration"] = data["duration"].str[7:]

    data["temperature"] = data["temperature"].map(lambda x: format(x, ".13f"))

    return data


def load_db(data):
    """
    loads database with data from pandas dataframe

    params: data (pandas dataframe)
    """
    conn = sqlite3.connect(db) #connects to the database
    if conn is not None:
        print("Loading data to database .....")
        data.to_sql(name="temperatures", con=conn, if_exists="replace")
        print("Loading data completed successfully")
        conn.close()

if __name__ == "__main__":
    data = read_task_data()
    clean_data = clean_data(data)
    load_db(clean_data)


