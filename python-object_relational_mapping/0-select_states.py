#!/usr/bin/python3
"""
Module name: 0-selected_states.

Contains something.
"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb

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
    c.execute("""SELECT * FROM states ORDER BY states.id ASC""")
    for row in c.fetchall():
        print(row)
