import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user ="root",
    passwd = "167167",
    database = "testdb"
)

mycursor =  mydb.cursor()

# mycursor.execute("SELECT * FROM students") # extracting all the data from the table
mycursor.execute("SELECT age FROM students") # extracting only age of the students
# myresult = mycursor.fetchall() # fetch all the entry
myresult  = mycursor.fetchone() # fetch only one entry

for row in myresult:
    print(row)