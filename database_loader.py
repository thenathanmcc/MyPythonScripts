"""
A simple script to load data from a text file into a PostgreSQL 12 database.
Written by Nathan McCulloch
"""


import psycopg2
from psycopg2 import Error


"""
Database connection parameters

"""
DATABASE_USER = ""
DATABASE_USER_PASSWORD = ""
DATABASE_HOST = ""
DATABASE_PORT = ""
DATABASE_NAME = ""

INSERT_QUERY = "INSERT INTO user_accounts (first_name, last_name) VALUES ('%s', '%s');"

TEXT_FILE = ""


try:
	# Attempt to establish connection with the database server
	connection = psycopg2.connect( 	user=DATABASE_USER,
								   	password=DATABASE_USER_PASSWORD,
									host=DATABASE_HOST,
									port=DATABASE_PORT,
									database=DATABASE_NAME )
	cursor = connection.cursor() # Get cursor

	# Attempt to open text file for reading
	file = open(TEXT_FILE, "r")
	line = file.readline();

	while (line != ''):
		if (len(line.split()) == 2): # Check there are exactly two values per line, otherwise ignore
			line = line.split()
			cursor.execute(INSERT_QUERY % (line[0], line[1]))
			connection.commit() # Commit transaction
		line = file.readline();

	new_row_count = cursor.rowcount
	print("Affected Row Count: ", new_row_count)

except (Exception, Error) as error:
	print("Error connecting to PostgreSQL:\n", error)
finally:
	if (connection):
		cursor.close()
		connection.close()
		print("PostgreSQL connection is now closed")
