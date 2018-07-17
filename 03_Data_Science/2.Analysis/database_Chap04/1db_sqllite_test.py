# 목적 : 데이터베이스를 메모리에 생성시 휘발성데이터임을 확인
import sqlite3

# Create an in-memory SQLite3 database
# Create a table called sales with four attributes
con = sqlite3.connect(':memory:')

# Query the sales table
cursor = con.execute("SELECT * FROM sales")
rows = cursor.fetchall()

#count the number of rows iin the output
row_counter = 0
for row in rows:
    print(row)
    row_counter += 1
print('Number of rows: {}'.format(row_counter))
