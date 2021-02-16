
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import StaleElementReferenceException

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

SIMILAR_ACCOUNT = "kyliejenner"
USERNAME = "hasib104_1"
PASSWORD = "Pp123456"

driver.get(url="https://www.instagram.com/")

time.sleep(3)
username = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
username.send_keys(USERNAME)

password = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
password.send_keys(PASSWORD)

log_in = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
log_in.click()

time.sleep(3)

notification_not_now = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
notification_not_now.click()


time.sleep(3)
search_bar = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
search_bar.send_keys(SIMILAR_ACCOUNT)
search_bar.send_keys(Keys.ENTER)

time.sleep(3)
selecting_account = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a')
selecting_account.click()

time.sleep(3)
followers = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
followers.click()


time.sleep(2)
follows = driver.find_elements_by_css_selector(".HVWg4 ._4EzTm button")
down_scroll = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
for follow in follows:
    try:
        follow.click()
        time.sleep(3)

        ###https://stackoverflow.com/questions/22709200/selenium-webdriver-scrolling-inside-a-div-popup/22729902
        ###https://stackoverflow.com/questions/38041974/selenium-scroll-inside-of-popup-div
        ###https://stackoverflow.com/questions/50317447/message-stale-element-reference-element-is-not-attached-to-the-page-document
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", down_scroll)

    except StaleElementReferenceException:
        pass