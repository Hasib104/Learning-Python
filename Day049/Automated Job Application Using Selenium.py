
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url="https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
time.sleep(1)

sign_in_button = driver.find_element_by_css_selector(".show .cta-modal__primary-btn")
sign_in_button.click()
time.sleep(2)

email = driver.find_element_by_css_selector(".login__form .form__input--floating #username")
email.send_keys("hasib104.python@gmail.com")

password = driver.find_element_by_css_selector(".login__form .form__input--floating #password")
password.send_keys("Pp654123")

sign_in_submit = driver.find_element_by_css_selector(".login__form .btn__primary--large")
sign_in_submit.click()

time.sleep(2)
first_offer = driver.find_element_by_css_selector(".jobs-search-results__list a")
first_offer.click()

time.sleep(2)
easy_apply = driver.find_element_by_css_selector(".relative .jobs-apply-button--top-card button")
easy_apply.click()

phone_no = driver.find_element_by_css_selector(".fb-single-line-text input")
phone_no.send_keys("1558986210")

next_button = driver.find_element_by_css_selector(".pv4 button")
next_button.click()

time.sleep(2)
next_button_1 = driver.find_element_by_css_selector(".pv4 .artdeco-button--primary span")
next_button_1.click()

submit_app = driver.find_element_by_css_selector(".pv4 .artdeco-button--primary span")
submit_app.click()

time.sleep(5)
driver.quit()