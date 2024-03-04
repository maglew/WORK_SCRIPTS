import cx_Oracle

connection = None
username = 'parus'
password = 'parusina'
'''
ip = '212.5.81.211'
port = 8546
SID = 'VFKNEW'

dsn = '172.28.200.59'
port = 1521
SID = 'VFKNEW'





host = '172.28.200.52'
port = 1521
SID = 'RUBIN'

host = '194.135.64.246'
port = 4226
SID = 'RUBIN'
'''
host = '172.28.5.140'
port = 1521
SID = 'META'
try:

    dsn = cx_Oracle.makedsn(host, 1521, service_name=SID)

    connection = cx_Oracle.connect(
        username,
        password,
        dsn)

    # show the version of the Oracle Database
    print(connection.version)

    thcur = connection.cursor()
    SQL_COMMAND = 'SELECT * from COMPANIES;'

    thcur.execute(SQL_COMMAND)


except cx_Oracle.Error as error:
    print(error)
finally:
    # release the connection
    if connection:
        connection.close()