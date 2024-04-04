from psycopg2 import connect

conn_string = "host='localhost' \
dbname='obsrv' user='obsrv_user' \
password='obsrv123'" 


# use connect function to establish the connection
conn = connect(conn_string)

cur= conn.cursor()
cur.execute("SELECT * FROM datasets;")
results=cur.fetchall()


cur.close()
conn.close()

for row in results:
    print(row)
