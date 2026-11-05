
from database import get_connection

try:
    conn = get_connection()
    print("MySQL connection successful!")
    print("Database:", conn.database)
    conn.close()
except Exception as error:
    print("Connection failed:", error)
