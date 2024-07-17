import mysql.connector

mydb = mysql.connector.connect(
    host ="localhost",
    user="root",
    passwd="167167",
    database="testdb"
)

mycursor = mydb.cursor()

# sql = "SELECT * FROM students WHERE age = 17" # extracting data of students whose age is 17
sql = "SELECT * FROM students WHERE name = 'Bob'" # extracting data of students whose name is 'Bob'

mycursor.execute(sql)

myresult = mycursor.fetchall()

for result in myresult:
    print(result)