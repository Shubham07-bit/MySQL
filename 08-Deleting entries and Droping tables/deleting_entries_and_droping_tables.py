import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="167167",
    database="testdb"
)

mycursor = mydb.cursor()

# sql = "DELETE FROM students WHERE name = 'Rachel'" # deleting the row from the table where name is 'Rachel'.
# sql = "DELETE FROM students WHERE age = 13" # deleting the row from the table where age is '13'.
# sql = "DROP TABLE students" # droping the table results in removing the table from the database. after executing this command you won't be able to find this table in the database.

'''
if you execute above command again it will give an error, so we will first check wether the table does exists or not.
'''

sql = "DROP TABLE IF EXISTS students"
mycursor.execute(sql)

mydb.commit()