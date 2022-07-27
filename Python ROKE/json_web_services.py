import shutil
import requests
import json


url = "http://jsonplaceholder.typicode.com/posts"

s = requests.get(url)
j = s.content.decode("utf-8")
#print(j)
myjson = json.loads(j)
#print(myjson)

#for i in range(0, 5):
    #print(myjson[i]["title"])

url = "http://placekitten.com/600/800"
ret = requests.get(url, stream=True)
outfile = open(f"kitten.png", "wb")
shutil.copyfileobj(ret.raw, outfile)
outfile.close()

# ........................
todos = "https://jsonplaceholder.typicode.com/todos"

todoreq = requests.get(todos)
todoj = todoreq.content.decode("utf-8")
todojson = json.loads(todoj)

#for item in todojson:
    #if item["completed"] == False:
        #print (item["title"])
        #print(item)

users = "https://jsonplaceholder.typicode.com/users"
usersreq = requests.get(users)
usersj = usersreq.content.decode("utf-8")
usersjson = json.loads(usersj)

for item in usersjson:
    if item["name"] == "Chelsey Dietrich":
        chelsey_address = item["address"]
        #print(item["address"])

        for piece in chelsey_address:
            print (f"{piece}: {chelsey_address[piece]}")



