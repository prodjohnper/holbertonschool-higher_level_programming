#!/usr/bin/python3
'''
    1-filter_states.py
    Description: Lists all states with a name
    starting with N from the database hbtn_0e_0_usa
'''
import MySQLdb
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        password=password,
        database=database
    )

    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    conn.close()
