#!/usr/bin/python3
'''
    5-filter_cities.py
    Description: Takes in the name of a state as an argument and lists
    all cities of that state, using the database hbtn_0e_4_usa
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
        """
            SELECT cities.name
            FROM cities
            INNER JOIN states
            ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
        """, (state,)
    )

    rows = cursor.fetchall()
    print(', '.join([row[0] for row in rows]))

    cursor.close()
    conn.close()
