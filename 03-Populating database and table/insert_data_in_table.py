import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "167167",
    database = "testdb"
)

mycursor = mydb.cursor()

sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"

student1 = ("Rachel", 22)

mycursor.execute(sqlFormula, student1) # every time you run this. data will be inserted in the database

mydb.commit() # at the end of insertion don't forget to commit the changes in database otherwise, it will not reflect in the database.