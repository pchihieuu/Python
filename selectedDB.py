import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         port='3306',
                                         database='electronics',
                                         user='root',
                                         password='')
    sql_select_Query = "select * from Laptop"
    # MySQLCursorDict creates a cursor that returns rows as dictionaries
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()

    print("Fetching each row using column name")
    for row in records:
        id = row["Id"]
        name = row["Name"]
        price = row["Price"]
        purchase_date = row["Purchase_date"]
        print(id, name, price, purchase_date)

except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if connection.is_connected():
        connection.close()
        cursor.close()
        print("MySQL connection is closed")
