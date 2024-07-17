import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="167167",
    database="testdb"
)

mycursor = mydb.cursor()

# mycursor.execute("SELECT * FROM students LIMIT 5") # Limiting output till 5 entries from starting

mycursor.execute("SELECT * FROM students LIMIT 4 OFFSET 3") # Limiting output from index(in terms of sql we can refer index as offset) 3.

myresult = mycursor.fetchall()

for result in myresult:
    print(result)