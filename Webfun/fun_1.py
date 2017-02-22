from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()

driver.get("https://www.google.com")

search_field = driver.find_element_by_id("lst_ib")
search_field.send_keys('1')