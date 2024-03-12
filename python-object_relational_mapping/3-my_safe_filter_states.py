#!/usr/bin/python3
'''
    3-my_safe_filter_states.py
    Description: Takes in arguments and displays all values in the states table
    of hbtn_0e_0_usa where name matches the argument. But this time, write one
    that is safe from MySQL injections
'''
import MySQLdb
import sys


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        password=password,
        database=database
    )

    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE BINARY name LIKE %s", (state,))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    conn.close()
