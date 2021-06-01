#!/usr/bin/python3
""" Script to list all states from database hbtn_0e_0_usa """

import MySQLdb


def state_list(mysql usename, mysql password, database name):
    """ Connect to mySQL server, print states listed in database, ascending id """

    #Open database connection
    usa_db = MySQLdb.connect("localhost", username, password, name)

    #prepare a cursor object
    cursor = usa_db.cursor()

    #find the states in the usa
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    #disconnect from server
    usa_db.close()

if __name__ == "__main__":
    state_list()
