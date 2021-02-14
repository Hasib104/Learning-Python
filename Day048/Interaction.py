
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

website = driver.get("https://en.wikipedia.org/wiki/Main_Page")
no_of_articles = driver.find_element_by_css_selector("#articlecount a")
print(no_of_articles.text)

#clicking button using click()
#no_of_articles.click()

#finding and clicking links using driver.find_element_by_link_text()
all_portals = driver.find_element_by_link_text("All portals")
#all_portals.click()

#Inputting keywords in Search field and pressing enter
search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)