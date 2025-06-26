#!/usr/bin/python3
"""
Module Name: 5-filter_cities.

Contains a script that takes an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
"""
from sys import argv
import MySQLdb


def filter_cities():
    """List cities of the input state."""
    mysql_username = argv[1]
    mysql_password = argv[2]
    db_name = argv[3]
    state_name = argv[4].split()[0]

    db = MySQLdb.connect(
        user=mysql_username,
        passwd=mysql_password,
        database=db_name,
        host='localhost',
        port=3306)
    c = db.cursor()
    query = "SELECT cities.name FROM cities "\
            "INNER JOIN states ON cities.state_id=states.id "\
            "WHERE BINARY states.name='{}' "\
            "ORDER BY cities.id ASC".format(state_name)
    c.execute(query)
    comma_list = []
    for row in c.fetchall():
        comma_list.append(row[0])
    print(", ".join(comma_list))
    c.close()
    db.close()


if __name__ == "__main__":
    filter_cities()
