import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()
mycursor.execute( "CREATE TABLE mammiferi (Id int(200), 
    Nome-proprio varchar(255),
    Razza varchar(255),
    Peso int(255),
    Età vaechar(255)")
