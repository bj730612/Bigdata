import csv
import MySQLdb
import sys

# Path to and name of a CSV input file
input_file = sys.argv[1]

# Connect to a MySQL database
con = MySQLdb.connect(host='localhost', port=3308, db='my_suppliers', user='bigdata', passwd='1111')
c = con.cursor()

# Read the CSV file and update the specific rows
file_reader = csv.reader(open(input_file, 'r', newline=''), delimiter=',')
header = next(file_reader, None)
for row in file_reader:
    data = []
    for column_index in range(len(header)):
        c.execute("""DELETE FROM Suppliers WHERE Supplier_Name='Supplier Z'""", data)
    if data != []:
        print(data)
con.commit()

# Query the Suppliers table
c.execute("SELECT * FROM Suppliers")
rows = c.fetchall()
for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(str(row[column_index]))
    print(output)
