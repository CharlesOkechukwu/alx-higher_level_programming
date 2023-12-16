#!/usr/bin/python3
"""module filter results by capital letter"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    """filter results by the name entered
    by user
    """
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           password=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name \
           LIKE BINARY '{}' ORDER BY states.id ASC".format(argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
