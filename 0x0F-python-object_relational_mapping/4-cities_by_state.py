#!/usr/bin/python3
"""Select cities by state"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    """select all cities in the cities table join result with states"""
    con = MySQLdb.connect(host="localhost", user=argv[1], password=argv[2],
                          port=3306, db=argv[3], charset="utf8")
    cur = con.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
                FROM cities join states ON cities.state_id = states.id
                ORDER BY cities.id ASC""")
    rows = cur.fetchall()
    if rows is not None:
        for row in rows:
            print(row)
