import mysql.connector
from config import database_info

mydb = mysql.connector.connect(host=database_info['host'],
                               user=database_info['login_id'],
                               password=database_info['password']
                               # database='mydatabase'
                               )
print(mydb)

mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE mydatabase")
mycursor.execute("SHOW DATABASES")

for database in mycursor:
    print(database)
