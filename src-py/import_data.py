import pandas as pd
import sqlite3
import sys
import os
import logging

from classifier import Classifier
from helper_functions import get_transactions_length, get_transactions, add_transactions
from constants import CONFIG_FOLDER

logger = logging.getLogger(__name__)
transactions = pd.read_csv(sys.argv[1])

classifier = Classifier()

inst_type = 'ws'

conn = sqlite3.connect(os.path.join(CONFIG_FOLDER, APP_NAME + ".db"))
cur = conn.cursor()

#cur.execute('DROP TABLE transactions')

cur.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY,
        date TEXT,
        type TEXT,
        description TEXT,
        amount REAL,
        category TEXT
    )
''')

transaction_num = get_transactions_length(conn)

if (transactions.columns.values == ['date','transaction','description','amount','balance']).all():
    inst_type = 'ws'

    transactions = transactions.drop(columns='balance')
    transactions.columns = ['date','type','description','amount']

    # If there are at least 10 transactions then predict categories
    if transaction_num >= 10:
        transactions['category'] = classifier.predict(transactions['description'])
    else:
        transactions['category'] = pd.NA

add_transactions(conn, transactions)

conn.commit()

print(get_transactions(conn))

conn.close()