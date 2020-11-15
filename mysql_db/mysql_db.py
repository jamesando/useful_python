import pymysql

# Insert the required connection details below
server = "XXXXX"
user = "XXXXX"
password = "XXXXX"
db = "XXXXX"

con = pymysql.connect(server, user, password, 'db')

try:

    with con.cursor() as cur:

        cur.execute('SELECT VERSION()')

        version = cur.fetchone()

        print(f'Database version: {version[0]}')

        con.close()

except:

    "Failed to connect to MySql Database"