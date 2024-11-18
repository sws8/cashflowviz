import sqlite3
import pandas as pd

def get_transactions_length(conn: sqlite3.Connection) -> int:
    '''Gets the number of transactions in the db'''
    return len(pd.read_sql('SELECT * FROM transactions', conn))

def get_transactions(conn: sqlite3.Connection) -> pd.DataFrame:
    '''Gets all the transactions in the db as a DataFrame'''
    return pd.read_sql('SELECT * FROM transactions', conn)

def add_transactions(conn: sqlite3.Connection, data: pd.DataFrame) -> None:
    '''Insert rows into the db'''
    data.to_sql('transactions', conn, if_exists='append', index=False)