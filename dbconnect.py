import mysql.connector
conn = mysql.connector.connect(host='localhost',password='040503', user='root')

if conn.is_connected():
    print("connection established")
