from bs4 import BeautifulSoup
import requests

url = "http://35.178.198.206/scarlet1.html"
ret = requests.get(url)
html = ret.content.decode("utf-8")
soup = BeautifulSoup(html, features="html.parser")

watson = soup.find_all("span", {"class": "watson"})
holmes = soup.find_all("span", {"class": "holmes"})
stamford = soup.find_all("span", {"class": "stamford"})

for line in watson:
    print("W: " + line.get_text().replace('”', '').replace('“', '').rstrip(','))

for line in holmes:
    print("H: " + line.get_text().replace('”', '').replace('“', '').rstrip(','))

