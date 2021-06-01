#!/usr/bin/python3
""" Script to list all states from database hbtn_0e_0_usa """

import MySQLdb
from sys import argv


if __name__ == "__main__":
    """ Connect to mySQL server, print states listed in database, ascending id """

    #Open database connection
    usa_db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])

    #prepare a cursor object
    cursor = usa_db.cursor()

    #find the states in the usa
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    #store, print the discovered data
    state_list = cursor.fetchall()
    print(state_list)

    #disconnect from server
    usa_db.close()
