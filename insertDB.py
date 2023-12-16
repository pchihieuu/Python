import mysql.connector

def insert_varibles_into_table(id, name, price, purchase_date):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             port='3306',
                                             database='electronics',
                                             user='root',
                                             password='')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date) 
                                VALUES (%s, %s, %s, %s) """

        record = (id, name, price, purchase_date)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print("Record inserted successfully into Laptop table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

insert_varibles_into_table(1, 'Asus Vivobook', 130000, '2023-12-04')
insert_varibles_into_table(2, 'HP Nitro 5', 130000, '2023-12-04')
insert_varibles_into_table(4, 'HP Pavilition', 20000, '2023-12-04')
insert_varibles_into_table(5, 'MacBook Pro 16GB', 600000, '2023-12-04')
insert_varibles_into_table(6, 'MackBook Air M1', 30000, '2023-12-04')
