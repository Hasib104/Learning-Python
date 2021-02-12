
import requests
from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.com/Western-Digital-Elements-Portable-External/dp/B06W55K9N6/ref=sr_1_1?dchild=1&qid=1613158346&s=computers-intl-ship&sr=1-1"
headers = {
    "Accept-Language" : "en-US,en;q=0.9,es;q=0.8,hi;q=0.7,bn;q=0.6",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
}
price_to_buy = float(70.00)
MY_EMAIL = "hasib104.python@gmail.com"
PASSWORD = "Pp123456"


response = requests.get(url=url, headers=headers)
web_page = response.text
#print(web_page)

soup = BeautifulSoup(web_page, "html.parser")
#print(soup.prettify())

price = soup.find(name="span", class_="a-size-medium a-color-price priceBlockBuyingPriceString").getText()
#print(price)
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
#print(price_as_float)

title = soup.find(name="span", class_="a-size-large product-title-word-break").getText()
#print(title)

if price_as_float < price_to_buy:
    message = f"{title} is now {price}."

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="hasibkamalaraf@gmail.com",
            msg=f"Subject:Amazon price alert!\n{message}\n{url}"
        )