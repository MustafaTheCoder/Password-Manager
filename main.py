import psycopg2

connection = psycopg2.connect(user = "postgres",
password = "singer2005*",
host = "127.0.0.1",
port = "5432",
database = "Test")

cursor = connection.cursor()
cursor.execute("Select * From products")
cursor.fetchall()