
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

website = driver.get("http://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element_by_name("fName")
f_name.send_keys("Hasib")

l_name = driver.find_element_by_name("lName")
l_name.send_keys("Kamal")

email = driver.find_element_by_name("email")
email.send_keys("hasib104.python@gmail.com")

submit = driver.find_element_by_class_name("btn-block")
submit.send_keys(Keys.ENTER)