#!/usr/bin/python3
"""
Module name: 1-filter_states.

Contains something a script that lists the states whose names start
with the capital letter 'N'.
"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    # def filter_states():
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
    c.execute("""SELECT * FROM states
            WHERE states.name LIKE %s
            ORDER BY states.id ASC""", ("N%",))
    for row in c.fetchall():
        print(row)

    c.close()
    db.close()

    # filter_states()
