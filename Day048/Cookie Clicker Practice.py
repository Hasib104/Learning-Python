
from selenium import webdriver
import time

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Get cookie to click on.
cookie = driver.find_element_by_id("cookie")

# Get upgrade item ids.
items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]
#print(item_ids)

timeout = time.time() + 3
five_min = time.time() + 60 * 5

while True:

    cookie.click()

    #finding money and making is int()
    money = driver.find_element_by_css_selector("#game #money")
    money_text_int = int(money.text)
    #print(money_text_int)

    prices = []
    if time.time() > timeout:
        #finding all the prices for upgrades
        finding_all_prices_tag = driver.find_elements_by_css_selector("#store b")

        #splitting the prices from names
        for price in finding_all_prices_tag:
            all_prices_tag_text = price.text
            if all_prices_tag_text != "":
                just_price_int = int(all_prices_tag_text.split("-")[1].strip().replace(",", ""))
                prices.append(just_price_int)
            #print(prices)

        #making a dictionary for upgrades price : id
        cookie_upgrades = {}
        for i in range(len(prices)):
            cookie_upgrades[prices[i]] = item_ids[i]
            #print(cookie_upgrades)

        #making a dictionary for affordable upgrades
        # affordable_upgrades = {}
        # for cost, id in cookie_upgrades.items():
        #     if money_text_int > cost:
        #         affordable_upgrades[cost] = id
        #         #print(affordable_upgrades)
        affordable_upgrades = {cost:id for (cost,id) in cookie_upgrades.items() if money_text_int > cost}

        #buying the highest upgrade
        highest_upgrade = max(affordable_upgrades)
        highest_upgrade_id = affordable_upgrades[highest_upgrade]
        driver.find_element_by_id(highest_upgrade_id).click()

        #adding a timeout so that the code doesnt crash(highest_upgrade = max(affordable_upgrades) \nValueError: max() arg is an empty sequence), this helps the game's score to increase.
        timeout = time.time() + 3

        if time.time() > five_min:

            cps = driver.find_element_by_css_selector("#game #cps").text
            print(cps)
            break
