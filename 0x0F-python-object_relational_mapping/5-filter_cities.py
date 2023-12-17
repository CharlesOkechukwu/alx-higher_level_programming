#!/usr/bin/python3
"""Select cities by state"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    """select all cities in the cities table join result with states"""
    con = MySQLdb.connect(host="localhost", user=argv[1], password=argv[2],
                          port=3306, db=argv[3], charset="utf8")
    cur = con.cursor()
    cur.execute("""SELECT cities.name
                FROM cities join states ON cities.state_id = states.id
                WHERE states.name LIKE BINARY %(state_name)s
                ORDER BY cities.id ASC""", {'state_name': argv[4]})
    rows = cur.fetchall()
    if rows is not None:
        print(", ".join([row[0] for row in rows]))
