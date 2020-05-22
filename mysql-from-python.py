import os
import pymysql

# Get username from workspace
# modify if running on another environment

username = os.getenv("AbnocChinwads")

# Connect to the database
connection = pymysql.connect(host= "localhost",
                            user=username,
                            password="",
                            db="Chinook")
try:
    # Run a query
    with connection.cursor() as cursor:
        sql = "select * from Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # CLose the connection, whether or not the above was successful
    connection.close()