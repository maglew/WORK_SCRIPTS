import pyodbc

host = '172.28.5.140'
port = '1521'
dbname = 'META'
driver = 'Microsoft Oracle ODBC Driver'
SID = host+","+port
#SID = host+"/"+dbname
username = 'parus'
password = 'parusina'



#connectionString = f'DRIVER={{Microsoft Oracle ODBC Driver}};SERVER={SID};DATABASE={dbname};UID={username};PWD={password}'

#connectionString = f'DRIVER={driver};SERVER={SID};DATABASE={dbname};UID={username};PWD={password}'

connectionString = (
    r"DRIVER={Microsoft Oracle ODBC Driver};"
    r"DBQ=META;"
    r"UID=parus;"
    r"PWD=parusina;"
)


'''
connectionString = ("Driver={Microsoft Oracle ODBC Driver};"
                      "Server={"+SID+"};"
                      "Database={"+dbname+"};"
                      "UID={"+username+"};"
                      "PWD={"+username+"};")
'''
print(connectionString)

conn = pyodbc.connect(connectionString)


SQL_QUERY = """
select * from COMPANIES;
"""

cursor = conn.cursor()
cursor.execute(SQL_QUERY)

records = cursor.fetchall()
for r in records:
    print(f"{r.RN}\t{r.NAME}\t{r.FULLNAME}")

cursor.close()
conn.close()