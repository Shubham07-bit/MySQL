import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="167167",
    database="testdb"
)

mycursor = mydb.cursor()

# sql = "SELECT * FROM students ORDER BY name ASC" # ordering output by name 'ASC'(ascending) order
# sql = "SELECT * FROM students ORDER BY name DESC" # ordering output by name 'DESC'(descending) order
# sql = "SELECT * FROM students ORDER BY age ASC" # ordering output by age 'ASC'(ascending) order
sql = "SELECT * FROM students ORDER BY age DESC" # ordering output by age 'DESC'(descending) order
mycursor.execute(sql)

myresult = mycursor.fetchall()

for result in myresult:
    print(result)