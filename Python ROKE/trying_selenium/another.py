from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import csv
import random

infile = open("comments.csv")

wd = webdriver.Chrome()
wd.get("http://35.178.198.206/index.html")

for line in csv.reader(infile, delimiter=","):

    carddetails = wd.find_element(By.LINK_TEXT, "Enter credit card details").click()

    namefield = wd.find_element(By.NAME, "cardholder").send_keys(line[0])
    time.sleep(1)

    cardnumber = wd.find_element(By.NAME, "cardnumber").send_keys(line[1])
    time.sleep(1)

    cardtype = wd.find_element(By.NAME, "cardtype").send_keys(line[2])
    time.sleep(1)

    ExpMonth = wd.find_element(By.NAME, "expirymonth").send_keys(line[3])
    time.sleep(1)

    ExpYear = wd.find_element(By.NAME, "expiryyear").send_keys(line[4])
    time.sleep(1)

    submit = wd.find_element(By.XPATH, "/html/body/form/input[6]").click()

    homelink = wd.find_element(By.LINK_TEXT, "Go back to index").click()

wd.quit()

infile.close()