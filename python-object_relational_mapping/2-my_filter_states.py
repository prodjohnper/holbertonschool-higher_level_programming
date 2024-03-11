#!/usr/bin/python3
'''
    2-my_filter_states.py
    Description: Takes in an argument and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument
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
        "SELECT * FROM states WHERE BINARY name LIKE '{}'".format(state))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    conn.close()
