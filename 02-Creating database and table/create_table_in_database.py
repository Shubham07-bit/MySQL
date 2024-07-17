import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "167167",
    database = "testdb"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))") #run only one time for creating a table, if table with this name already exists then it will throw an error
mycursor.execute("SHOW TABLES")

for tb in mycursor:
    print(tb)