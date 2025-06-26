#!/usr/bin/python3
"""
Module Name: 4-cities_by_state.

Contains a script that takes an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
"""
from sys import argv
import MySQLdb


def cities_by_state():
    """List values for which states matches the desired state name."""
    mysql_username = argv[1]
    mysql_password = argv[2]
    db_name = argv[3]

    db = MySQLdb.connect(
        user=mysql_username,
        passwd=mysql_password,
        database=db_name,
        host='localhost',
        port=3306)
    c = db.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities "\
            "INNER JOIN states ON cities.state_id=states.id "\
            "ORDER BY cities.id ASC"
    c.execute(query)
    for row in c.fetchall():
        print(row)

    c.close()
    db.close()


if __name__ == "__main__":
    cities_by_state()
