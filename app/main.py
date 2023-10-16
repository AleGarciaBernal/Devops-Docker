# main.py

import mysql.connector

mydb = mysql.connector.connect(
  host="db",
  user="root",
  password="example",
  database="mydatabase"
)

print(mydb)
