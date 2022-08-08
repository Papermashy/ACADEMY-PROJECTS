import requests

for i in range(1, 101):
    url = f"http://127.0.0.1:8000/fizzbuzz?nNum={i}"
    ret = requests.get(url)
    body = ret.content.decode("utf-8")
    print(body)
