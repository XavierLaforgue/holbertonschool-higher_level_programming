#!/usr/bin/python3
"""
Module Name: 2-my_filter_states.

Contains a script that takes an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
"""
from sys import argv
import MySQLdb


def my_filter_states():
    """List values for which states matches the desired state name."""
    mysql_username = argv[1]
    mysql_password = argv[2]
    db_name = argv[3]
    state_name = argv[4]

    db = MySQLdb.connect(
        user=mysql_username,
        passwd=mysql_password,
        database=db_name,
        host='localhost',
        port=3306)
    c = db.cursor()
    query = "SELECT * FROM states "\
            "WHERE BINARY name='{}' "\
            "ORDER BY states.id ASC".format(state_name)
    c.execute(query)
    for row in c.fetchall():
        print(row)

    c.close()
    db.close()


if __name__ == "__main__":
    my_filter_states()
