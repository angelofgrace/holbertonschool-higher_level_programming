#!/usr/bin/python3
""" Script to list all states from database hbtn_0e_0_usa """


if __name__ == "__main__":
""" Connect to mySQL server, print states listed in database, ascending id """

    import MySQLdb
    from sys import argv

    #Open database connection
    usa_db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])

    #prepare a cursor object
    cursor = usa_db.cursor()

    #find the states in the usa
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    #disconnect from server
    usa_db.close()
