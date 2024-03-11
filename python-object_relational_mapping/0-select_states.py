#!/usr/bin/python3
'''
    0-select_states.py
    
    Description: Lists all states from the database hbtn_0e_0_usa
'''
import MySQLdb
from sys import argv

if __name__ == "__main__":

    username = argv[1]
    password = argv[2]
    database = argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        password=password,
        database=database
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    conn.close()
