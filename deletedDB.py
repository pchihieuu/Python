import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         port='3306',
                                         database='electronics',
                                         user='root',
                                         password='')

    cursor = connection.cursor()
    sql_Delete_query = """Delete from Laptop where id = %s"""
    records_to_delete = [(6,), (5,)]
    cursor.executemany(sql_Delete_query, records_to_delete)
    connection.commit()
    print(cursor.rowcount, " Record Deleted successfully")

except mysql.connector.Error as error:
    print("Failed to Delete records from MySQL table: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
