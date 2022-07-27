import sqlite3

# connect to the database or create if it doesn't exist
connection = sqlite3.connect("people.db")
cur = connection.cursor()

# create a table if it doesn't exist
s = "create table if not exists persons(name text, address text, email text)"
cur.execute(s)

s = "insert into persons(name, address, email) values('Alice', '1 High Street', 'alice@example.com')"
cur.execute(s)

s = "select * from persons"
cur.execute(s)
rs = cur.fetchall()
print(rs)

s = "update persons set address = '1 Main street' where name = 'Alice'"
cur.execute(s)

s = "select * from persons"
cur.execute(s)
rs = cur.fetchall()
print(rs)

s = "delete from persons where name = 'Alice'"
cur.execute(s)
rs = cur.fetchall()
print(rs)

connection.commit()
connection.close()


