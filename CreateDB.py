import mysql.connector
# xu ly ngoai le
try:
    # Khai bao ket noi
    connection = mysql.connector.connect(host='localhost',
                                         port='3306',
                                         database='electronics',
                                         user='root',
                                         password='')
    # Thuc hien khoi tao table Laptop
    mySql_Create_Table_Query = """CREATE TABLE Laptop ( 
                             Id int(11) NOT NULL,
                             Name varchar(250) NOT NULL,
                             Price float NOT NULL,
                             Purchase_date Date NOT NULL,
                             PRIMARY KEY (Id)) """
    # Thuc hien ket noi
    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    # In thong bao ket noi thanh cong
    print("Laptop Table created successfully ")

except mysql.connector.Error as error: # thong bao ket noi khong thanh cong
    print("Failed to create table in MySQL: {}".format(error))
finally:
    #Neu ket noi thanh cong thi...
    if connection.is_connected():
        # Dong ket noi
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
