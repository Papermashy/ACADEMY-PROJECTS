from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import csv
import random

infile = open("MOCK_DATA.csv")
cities = ["Paris", "Berlin"]
wd = webdriver.Chrome()
wd.get("http://35.178.198.206/index.html")

for line in csv.reader(infile, delimiter=","):

    wd.find_element(By.NAME, "name").send_keys(line[0])
    wd.find_element(By.NAME, "commenttext").send_keys(line[1])

    locationfield = wd.find_element(By.NAME, "commentlocation")
    selectlocation = Select(locationfield).select_by_visible_text(random.choice(cities))

    locationfield.submit()

    time.sleep(2)

    wd.find_element(By.LINK_TEXT, "Back to Home").click()
    time.sleep(5)

wd.quit()

infile.close()
