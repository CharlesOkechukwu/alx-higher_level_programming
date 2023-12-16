#!/usr/bin/python3
"""list all states in a database module"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """print out all states stored in
    a database module
    """
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           password=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
