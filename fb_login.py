from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass

usr = raw_input("Enter your facebook username : ")
pwd = getpass("Enter your facebook password : ")

browser = webdriver.Firefox()

browser.get('https://www.facebook.com')
assert 'Facebook' in browser.title

elem_user = browser.find_element_by_id("email")
elem_pass = browser.find_element_by_id("pass")
elem_user.send_keys(usr)
elem_pass.send_keys(pwd)
elem_pass.send_keys(Keys.RETURN)



