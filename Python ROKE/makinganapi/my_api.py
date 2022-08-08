from fastapi import FastAPI
import json
from pydantic import BaseModel

j = """
[
    {
        "id": 1,
        "name": "apple",
        "quantity": 50
    },
    {
        "id": 2,
        "name": "banana",
        "quantity": 100
    },
    {
        "id": 3,
        "name": "orange",
        "quantity": 5000
    }
]
"""

app = FastAPI()
fruits = json.loads(j)
nextid = 4


class Fruit(BaseModel):
    name: str
    quantity: int


@app.get("/fruit")
def api_get_fruit(id: int):
    if id == 0:
        res = fruits
    else:
        res = {"message": "No matching fruit found"}
        for fruit in fruits:
            if fruit["id"] == id:
                res = fruit
                break

    return res


@app.post("/newfruit")
def api_newfruit(fruit: Fruit):
    global nextid
    global fruits

    newfruit = {}
    newfruit["id"] = nextid
    newfruit["name"] = fruit.name
    newfruit["quantity"] = fruit.quantity
    fruits.append(newfruit)
    nextid += 1

    return newfruit


@app.get("/hello")
def api_hello():
    return {"message": "Hello world"}


@app.get("/addtwo")
def api_addtwo(nFirst: int, nSecond: int):
    n = nFirst + nSecond
    return {"result": n}


@app.get("/fizzbuzz")
def api_fizzbuzz(nNum: int):
    if nNum % 3 == 0 and nNum % 5 == 0:
        return {"value": "FizzBuzz"}
    elif nNum % 3 == 0:
        return {"value": "Fizz"}
    elif nNum % 5 == 0:
        return {"value": "Buzz"}
    else:
        return {"value": f"{nNum}"}



