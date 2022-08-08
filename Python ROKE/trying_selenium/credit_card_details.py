from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

wd = webdriver.Chrome()

wd.get("http://35.178.198.206")

card_link = wd.find_element(By.LINK_TEXT, "Enter credit card details")
card_link.click()

name_field = wd.find_element(By.NAME, "cardholder")
name_field.send_keys("Seamus")

name_field = wd.find_element(By.NAME, "cardnumber")
name_field.send_keys("29384723")

name_field = wd.find_element(By.NAME, "cardtype")
name_field.send_keys("Fastercard")

name_field = wd.find_element(By.NAME, "expirymonth")
name_field.send_keys("01")

name_field = wd.find_element(By.NAME, "expiryyear")
name_field.send_keys("26")

time.sleep(2)

name_field.submit()

time.sleep(5)

wd.quit()
