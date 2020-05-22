import os
import datetime
import pymysql

# Get username from workspace
# modify if running on another environment

username = os.getenv("AbnocChinwads")

# Connect to the database
connection = pymysql.connect(host="localhost",
                             user=username,
                             password="",
                             db="Chinook")
try:
    # Run a query
    with connection.cursor() as cursor:
        list_of_names = ['Jim', 'Bob', 'Fred']
        # Prepare a string with the same number of
        # placeholders as in list_of_names
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute("Delete from Friends where name in ({});".format(format_strings),
                       list_of_names)
        connection.commit()

finally:
    # CLose the connection, whether or not the above was successful
    connection.close()
