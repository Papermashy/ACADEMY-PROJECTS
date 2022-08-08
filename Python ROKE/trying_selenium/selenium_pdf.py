import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime


wd = webdriver.Chrome()
# go to the cards query page and enter a query
wd.get("http://35.178.198.206/getcard.html")
wd.find_element(By.NAME, "cardholder").send_keys("Betty")
wd.find_element(By.NAME, "cardholder").submit()

# pause while the page loads
time.sleep(2)
# get a reference to the table
table = wd.find_element(By.CSS_SELECTOR, "html > body > table")
# find the number of rows in the table
rows = table.find_elements(By.XPATH, "//tr")
print("Number of rows : {}".format(len(rows)))

# loop round each row
i = 1
for i in range(len(rows)):
    # count the columns on this row
    columns = rows[i].find_elements(By.XPATH, "td")
    print()
    print("Row {} has {} columns".format(i, len(columns)))
    # loop round each column
    j = 0
    for j in range(len(columns)):
            cell_data = columns[j].text
            print("{}, {} : {}".format(i, j, cell_data))
            if j == 5 and int(cell_data) < (datetime.date.today().year):
                print ("!This card has expired!")
            j += 1
    i += 1

