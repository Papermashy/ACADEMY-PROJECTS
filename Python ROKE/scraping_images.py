from bs4 import BeautifulSoup
import requests
import re

image_url = "http://35.178.198.206/bigpictures.html"

def get_soup(url):
    ret = requests.get(url)
    html = ret.content.decode("utf-8")
    my_soup = BeautifulSoup(html, features="html.parser")
    return my_soup

soup = get_soup(image_url)

p = re.compile(".*\.jpg")
links = soup.find_all("a", {"href": p})

full_urls = []

for link in links:
    full_urls.append("http://35.178.198.206/" + link.attrs["href"])

print(full_urls)

for link in full_urls:
    ret = requests.get(link)
    file = open(link.removeprefix("http://35.178.198.206/img/"), "wb")
    file.write(ret.content)
    file.close()
