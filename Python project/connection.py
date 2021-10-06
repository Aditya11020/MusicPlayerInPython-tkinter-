import pyodbc
conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=DESKTOP-QKA9C3N\acer"
    "Database=master;"
    "Trusted_Connection=yes;"
)
def read(conn):
    cursor = conn.cursor()
    cursor.execute("select * from Course")
    row = list(cursor)
    
    print(row)
read(conn)
