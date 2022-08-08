from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

wd = webdriver.Chrome()

wd.get("http://35.178.198.206")

name_field = wd.find_element(By.NAME, "name")
name_field.send_keys("A crab")

comment_field = wd.find_element(By.NAME, "commenttext")
comment_field.send_keys("*clacking of pincers*")

location_field = wd.find_element(By.NAME, "commentlocation")
select_location = Select(location_field)
select_location.select_by_visible_text("Berlin")

time.sleep(2)

name_field.submit()

time.sleep(5)

homelink = wd.find_element(By.LINK_TEXT, "Back to Home")
homelink.click()

wd.quit()

