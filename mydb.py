import mysql.connector

database = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'mysql123'

	)

# prepare a cursor object
cursorObject = database.cursor()

# create a database
cursorObject.execute("CREATE DATABASE softwareco")

print("All Done!")
