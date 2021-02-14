
from selenium import webdriver
url = "https://www.amazon.com/Western-Digital-Elements-Portable-External/dp/B06W55K9N6/ref=sr_1_1?dchild=1&qid=1613158346&s=computers-intl-ship&sr=1-1"
chrome_driver_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

#driver.get("https://www.amazon.com/Western-Digital-Elements-Portable-External/dp/B06W55K9N6/ref=sr_1_1?dchild=1&qid=1613158346&s=computers-intl-ship&sr=1-1")
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)


# search_bar = driver.find_element_by_name("field-keywords")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("class"))


# driver.get("https://www.python.org/")
# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# doc_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(doc_link.text)
#
# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)
#
# #driver.close()
# driver.quit()

website = driver.get("https://www.python.org/")
event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget ul a")
#new_dict = {new_key : new_value for (key,value) in dict.items()}
events = {}

for item in range(len(event_times)):
    events[item] = {
        "time" : event_times[item].text,
        "name" : event_names[item].text,
    }
print(events)
driver.quit()