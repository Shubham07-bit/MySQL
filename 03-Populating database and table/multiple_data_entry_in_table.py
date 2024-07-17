import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "167167",
    database = "testdb"
)

mycursor = mydb.cursor()

sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"
students = [("Bob",12),
            ("Amanda", 32),
            ("Jacob", 21),
            ("Avi", 28),
            ("Michelle", 17)]

mycursor.executemany(sqlFormula, students)

mydb.commit()