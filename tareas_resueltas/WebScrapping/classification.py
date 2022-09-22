from novela import Novel
from sqlite import SqliteStorage
import pandas as pd
import sqlite3

def main():
    # Read sqlite query results into a pandas DataFrame
    with SqliteStorage(r"novelas.db") as sqliteStorage:
        df = pd.read_sql_query("SELECT * from novels", sqliteStorage)

        # Verify that result of SQL query is stored in the dataframe
        print(df.head())

main()
