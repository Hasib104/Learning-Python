
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

FB_EMAIL = "hasib104.python@gmail.com"
FB_PASSWORD = "Pp123456"

driver.get(url="http://www.tinder.com")
time.sleep(2)

i_accept_button = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
i_accept_button.click()

time.sleep(2)
log_in = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
log_in.click()

time.sleep(2)
log_in_fb = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
log_in_fb.click()

time.sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

#Login and hit enter
email = driver.find_element_by_xpath('//*[@id="email"]')
password = driver.find_element_by_xpath('//*[@id="pass"]')
email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)

#Switch back to Tinder window
driver.switch_to.window(base_window)
print(driver.title)

time.sleep(5)

#Allow location
allow_location_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

time.sleep(2)
#Disallow notifications
notifications_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

for n in range(100):

    time.sleep(2)

    try:
        like_button = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    except:
        try:
            no_thanks = driver.find_element_by_xpath('// *[ @ id = "modal-manager"] / div / div / button[2]')
            no_thanks.click()
        except:

            subscription = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[3]/button[2]')
            subscription.click()
driver.quit()