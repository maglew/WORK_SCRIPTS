import oracledb

username = 'PARUS'
password = 'parusina'

host = '172.28.5.140'
port = 1521
SID = 'META'
'''
host = '172.28.200.149'
port = 1521
SID = 'MSUTEST'

host = '172.28.200.52'
port = 1521
SID = 'RUBIN'

cp = oracledb.ConnectParams(host=host, port=port, service_name=SID)
dsn = cp.get_connect_string()

#dsn="172.28.5.140:1521/META"

print(dsn)

#connection = oracledb.connect(user=username,password=password, dsn=dsn)
#print("Successfully connected to Oracle Database")

#connection.close()

#with oracledb.connect(user=username,password=password,host=host,port=port,service_name=SID) as connection:
with oracledb.connect(user=username,password=password, dsn=dsn) as connection:
    print("Successfully connected to Oracle Database")
    print(connection.clientinfo)
    with connection.cursor() as cursor:
        for row in cursor.execute("select * from COMPANIES"):
            print(row)

    connection.close()
    print("connection closed")
'''
connection = ''
cursor = ''

try:
    cp = oracledb.ConnectParams(host=host, port=port, service_name=SID)
    dsn = cp.get_connect_string()
    # Подключиться к существующей базе данных
    #connection = oracledb.connect(user=username, password=password, host=host, port=port, service_name=SID)
    connection = oracledb.connect(user=username,password=password, dsn=dsn)

    # Создайте курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    # SQL-запрос для создания новой таблицы
    SQL_query = "select * from COMPANIES;"
    cursor.execute(SQL_query)
    print("Результат", cursor.fetchall())

except (Exception) as error:
    print("Ошибка при работе с ORACLE", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с ORACLE закрыто")

