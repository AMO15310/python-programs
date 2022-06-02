#!/bin/python3
from selenium import webdriver
import time
#password = Enter your password here
#username = "Enter your regestration number here"
driver = webdriver.Firefox()
driver.get("http://masomo1.kyu.ac.ke")
element =driver.find_element_by_id("username")
element.send_keys(username)
time.sleep(2)
element = driver.find_element_by_id("password")
element.send_keys(password)
time.sleep(2)
element = driver.find_element_by_id("loginbtn").click()
