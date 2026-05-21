import mysql.connector

# Conectando ao banco de dados.
connection = mysql.connector.connect( 
    host="localhost",
    user="root",
    password=""
)

print("Conectado!")

