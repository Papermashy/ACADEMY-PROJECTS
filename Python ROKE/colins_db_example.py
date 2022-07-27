import sqlite3
import csv

def print_data():
    cur.execute("select * from books where author = 'Austen, Jane' order by author")
    res = cur.fetchall()
    print(res)

con = sqlite3.connect("books.db")
cur = con.cursor()

cur.execute("create table if not exists books (title text, author text)")
con.commit()

cur.execute("insert into books values('War and Peace', 'Tolstoy, Leo')")
cur.execute("insert into books values('Pride and Prejudice', 'Austen, Jane')")
cur.execute("insert into books values('Great Expectations', 'Dickens, Charles')")
con.commit()

bookdata = [("Jude the Obscure", "Hardy, Thomas"),
            ("Middlemarch", "Eliot, George"),
            ("Animal Farm", "Orwell, George")]
cur.executemany("insert into books values(?, ?)", bookdata)
con.commit()

infile = open("mycsv.csv")
for line in csv.reader(infile, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True):
    cur.execute("insert into books values(?, ?)", line)
infile.close()
con.commit()

print_data()


con.close()

