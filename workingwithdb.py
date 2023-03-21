import sqlite3

#create a new database 
conn = sqlite3.connect("dbfile.db")

#if a table exists already drop it
conn.execute('DROP TABLE IF EXISTS CUSTOMER;')

conn.execute(''' CREATE TABLE CUSTOMER(
    ID INT NOT NULL PRIMARY KEY,
    NAME TEXT NOT NULL,
    AGE INT NOT NULL
);

''')

conn.execute(''' INSERT INTO CUSTOMER (ID, NAME, AGE) 
VALUES(1, "AYOBAMI", 24);

''')

#get the content of the db file
fetch_all = conn.execute('''SELECT * FROM CUSTOMER;

''')

for row in fetch_all: #iterates throught the db table to print each tuples.
    print(row)

conn.close()