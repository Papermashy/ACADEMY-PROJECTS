from fastapi import FastAPI
import json
from pydantic import BaseModel
import random
import sqlite3

j = """
[
    {
        "id": 1,
        "author": "Jane Austen",
        "title": "Pride and Prejudice",
        "year": 1813
    }
]
"""

connection = sqlite3.connect("library.db")
cur = connection.cursor()
app = FastAPI()
books = json.loads(j)
sql = "create table if not exists books(id integer, author text, title text, year integer)"
cur.execute(sql)


sql = "insert into books(id, author, title, year) values (1, 'Jane Austen', 'Pride and Prejudice', 1813)"
cur.execute(sql)

nextid = 2


class Book(BaseModel):
    author: str
    title: str
    year: int


@app.get("/book")
def api_get_book(id: int):

    if id == 0:
        res = books
    else:
        res = {"message": "No matching fruit found"}
        req = f"select * from books where id == {id}"
        cur.execute(req)
        res = cur.fetchall()

    return res


@app.post("/newbook")
def api_newbook(book: Book):
    global nextid
    global books

    newbook = {}
    newbook["id"] = nextid
    newbook["author"] = book.author
    newbook["title"] = book.title
    newbook["year"] = book.year
    books.append(newbook)
    nextid += 1

    return newbook


@app.get("/randombook")
def api_randombook():
    r = random.randint(0, len(books)-1)
    return books[r]


@app.get("/hello")
def api_hello():
    return {"message": "Hello world"}
