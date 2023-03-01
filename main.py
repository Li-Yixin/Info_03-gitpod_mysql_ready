import mysql.connector

mydb = import mysql.connector(
  host="localhost",
  user="root",
  password=""
  database="mydatabase"
)

mycursor = mydb.cursor()   #crea in python un cursore#

mycursor.execute("CREATE DATABASE mydatabase")