#!/usr/bin/python3
"""This script connects to a MySQL database and retrieves all states from the 'states' table."""
from sys import argv

import MySQLdb

if __name__ == "__main__":
    mysql_username, mysql_password, mysql_db_name = argv[1], argv[2], argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=mysql_db_name,
    )
    cursor = db.cursor()
    all_states = cursor.execute("SELECT * FROM states ORDER BY id ASC")

    for i in cursor.fetchall():
        print(i)
    # Close the cursor and database connection
    cursor.close()
    db.close()
