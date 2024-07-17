import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="167167",
    database="testdb"
)

mycursor = mydb.cursor()

sql = "UPDATE students SET age = 13 WHERE name = 'Bob'" # updating the age of a student whose name is Bob

mycursor.execute(sql)

mydb.commit()
