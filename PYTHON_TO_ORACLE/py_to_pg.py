import psycopg2

from psycopg2 import Error
#from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


ip = '172.28.30.32'
port = 5432
user = 'parus'
password = 'parusina'
database = 'new'
try:
    # Подключиться к существующей базе данных
    connection = psycopg2.connect(user=user,
                                  password=password,
                                  host=ip,
                                  port=port,
                                  database=database)

    # Создайте курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    # SQL-запрос для создания новой таблицы
    SQL_query = '''SELECT * from COMPANIES; '''
    cursor.execute(SQL_query)
    print("Результат", cursor.fetchall())

    # Выполнение команды:
    cursor.execute(SQL_query)


except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")