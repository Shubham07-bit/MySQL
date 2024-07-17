import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="167167",
    database="testdb"
)

mycursor = mydb.cursor()

'''
Using wildcard characters we can fetch data from the table. 
eg: we just know about initals, includes or end of the name or data, anything we know we can just write wild card characters between them
'''

sql = "SELECT * FROM students WHERE name LIKE '%ac%'"
sql2 = "SELECT * FROM students WHERE name = %s"

# mycursor.execute(sql)
mycursor.execute(sql2, ("Rachel",))

myresult = mycursor.fetchall()

for result in myresult:
    print(result)