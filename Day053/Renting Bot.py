
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

ZILLOW = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.83501662207031%2C%22east%22%3A-122.03164137792969%2C%22south%22%3A37.69274928823367%2C%22north%22%3A37.85774156544393%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
GOOGLE = "https://docs.google.com/forms/d/e/1FAIpQLSdW1VD4odNygk1LtZpeQS-J7gJZPArH8IqmHceDUnwv15orqA/viewform?usp=sf_link"

response = requests.get(url=ZILLOW, headers=header)
data = response.text
soup = BeautifulSoup(data, "html.parser")

all_links_with_elements = soup.select(".list-card-info a")
all_links = []

for link in all_links_with_elements:
    href = link["href"]

    if "http" not in href:
        all_links.append(f"https://www.zillow.com/{href}")
    else:
        all_links.append(href)

#print(all_links)

all_addresses_with_elements = soup.select(".list-card-info address")
all_addresses = []

for address in all_addresses_with_elements:
    text = address.getText()
    all_addresses.append(text)

#print(all_addresses)

all_prices_with_elements = soup.select(".list-card-heading div")
all_prices = []

for price in all_prices_with_elements:
    rent = price.getText()
    all_prices.append(rent)

#print(all_prices)

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

for item in range(len(all_links)):
    driver.get(GOOGLE)

    time.sleep(3)

    property_address = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    property_address.send_keys(all_addresses[item])

    property_rent = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    property_rent.send_keys(all_prices[item])

    property_link = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    property_link.send_keys(all_links[item])

    submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
    submit.click()