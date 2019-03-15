# MYSQL-python / DB test
# Database = TestDB
# Table = TestTable

import MySQLdb

# Open database Connection
db=MySQLdb.connect('localhost','root','1234567890','TestDB')
# prepare a cursor object using cursor() method
cursor =db.cursor()

# execute SQL query using execute() method
cursor.execute("select * from TestTable")

try:
    # Fetch a single row using fetchome method
    results = cursor.fetchall()
    for row in results:
            Pin = row[0]
            Location = row[1]
            print ("Pin=%s, Location=%s" % (Pin, Location))
except:
    print ("Error: unable to fetch data")

db.close()
