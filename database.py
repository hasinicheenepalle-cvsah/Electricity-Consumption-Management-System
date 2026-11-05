
import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Cvsah@589",
        database="electricity_analysis",
        port=3306
    )
    return connection
