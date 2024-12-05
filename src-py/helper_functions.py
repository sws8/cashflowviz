import sqlite3
import pandas as pd

from import_data import logger

def get_transactions_length(conn: sqlite3.Connection) -> int:
    '''Gets the number of transactions in the db'''
    try:
        length = len(pd.read_sql('SELECT * FROM transactions', conn))
    except Exception as e:
        logger.error(f"Unable to get length of transactions db: {e}")
        length = -1
    return length

def get_transactions(conn: sqlite3.Connection) -> pd.DataFrame:
    '''Gets all the transactions in the db as a DataFrame'''
    try:
        transactions = pd.read_sql('SELECT * FROM transactions', conn)
    except Exception as e:
        logger.error(f"Unable to get transactions: {e}")
        transactions = pd.DataFrame()
    return transactions

def add_transactions(conn: sqlite3.Connection, data: pd.DataFrame) -> None:
    '''Insert rows into the db'''
    try:
        data.to_sql('transactions', conn, if_exists='append', index=False)
    except Exception as e:
        logger.error(f"Unable to add transactions to the db: {e}")

def update_transactions(conn: sqlite3.Connection, rows_to_update: list[tuple]) -> None:
    '''Edit existing transactions in the db'''
    try:
        conn.executemany('''
            UPDATE transactions
            SET date = ?, type = ?, description = ?, amount = ?, category = ?
            WHERE id = ?
        ''', rows_to_update)
    except sqlite3.Error as e:
        logger.error(f"Unable to edit transactions: {e}")