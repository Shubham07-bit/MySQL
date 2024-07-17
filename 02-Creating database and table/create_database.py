import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "167167"
)

mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE testdb") # only run first time when database is not created with this name, otherwise this will give an error that 'Can't create database 'testdb'; database exists'
mycursor.execute("SHOW DATABASES")

for db in mycursor:
    print(db)