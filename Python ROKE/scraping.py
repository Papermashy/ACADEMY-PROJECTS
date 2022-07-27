from bs4 import BeautifulSoup
import requests

url = "http://35.178.198.206/index.html"
ret = requests.get(url)
#print(ret.status_code)

html = ret.content.decode("utf-8")

soup = BeautifulSoup(html, features="html.parser")

tds = soup.find_all('td')

#for td in tds:
    #print(td.get_text())

hrds = soup.find_all('h2')

#for hd in hrds:
    #print(hd.get_text())

links = soup.find_all("a")
#for link in links:
    #print(link.get_text())


url = "http://35.178.198.206/styled.html"
ret = requests.get(url)

html = ret.content.decode("utf-8")

soup = BeautifulSoup(html, features="html.parser")

styledtext = soup.find_all("div", {"id": "id1"})
#print(styledtext)

#for item in styledtext:
    #print (item.get_text())

