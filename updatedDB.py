import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         port='3306',
                                         database='electronics',
                                         user='root',
                                         password='')
    cursor = connection.cursor()

    print("Before updating a record ")
    sql_select_query = """select * from Laptop where id = 2"""
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)

    # Update single record now
    sql_update_query = """Update Laptop set Purchase_date = "2023-12-05" where id = 2"""
    cursor.execute(sql_update_query)
    connection.commit()
    print("Record Updated successfully ")

    print("After updating record ")
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)

except mysql.connector.Error as error:
    print("Failed to update table record: {}".format(error))
finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")
