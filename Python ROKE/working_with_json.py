import json

books = """
[
    {
        "author": "W Somerset Maugham",
        "title": "The Moon and Sixpence"
    },
    {
        "author": "Leo Tolstoy",
        "title": "War and Peace"
    },
    {
        "author": "Charles Dickens",
        "title": "Great Expectations"
    },
    {   
        "author": "Jane Austen",
        "title": "Sense and Sensibility"
    }

]

"""

print(type(books))
j = json.loads(books)
print(type(j))

for book in j:
    print(book["author"])

person = {"Name": "Alice", "Address": "1 Main Street"}
new = json.dumps(person)

print(new)
print(type(new))

for book in j:
    if book["author"] == "Jane Austen":
        print(book["title"])

# read JSON from a file

infile = open("fruits.json")
fruits = json.load(infile)
print(type(fruits))

for fruit in fruits:
    print(fruit["name"])


