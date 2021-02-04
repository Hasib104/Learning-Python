
import requests
from twilio.rest import Client
import html

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
MY_STOCK_API = "EIEWIJHUPO06DYPK"
MY_NEWS_API = "b364cfcc37ae44d48046fc280e6b2658"
#MY_API = "EIEWIJHUPO06DYPK"

ACCOUNT_SID = "Twilio"
AUTH_TOKEN = "Twilio"

parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey" : MY_STOCK_API,
}

response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
#print(data)
#data_list = [new_item for item in List]
data_list = [value for (key, value) in data.items()]
#print(data_list)

yesterday_data = data_list[0]
print(yesterday_data)
yesterday_closing_price = yesterday_data["4. close"]
#print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
#print(day_before_yesterday_closing_price)

#Using absolute function
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
#print(difference)

diff_percent = (difference / float(yesterday_closing_price)) * 100
#print(diff_percent)

if diff_percent > 2:
    news_parameters = {
        "apiKey" : MY_NEWS_API,
        "qInTitle" : COMPANY_NAME,
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params= news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    three_articles = news_data["articles"][:3]
    #print(three_articles)

#data_list = [new_item for item in List]
formatted_article = [f"Headline: {articles['title']}. \nBrief: {articles['description']}" for articles in three_articles]
print(formatted_article)

client = Client(ACCOUNT_SID, AUTH_TOKEN)
for article in formatted_article:
    message = client.messages \
        .create(
        body=article.encode('utf-8'),
        from_='+19362336529',
        to='+8801558985075'
    )
