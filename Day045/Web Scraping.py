
from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
#print(soup.title)
print(soup.prettify())

"""#Finding first article name, href,upvote"""
# heading = soup.find(name="a", class_="storylink")
# #print(heading)
# article_text = heading.getText()
# print(article_text)
# article_href = heading.get("href")
# print(article_href)
# article_upvote = soup.find(name="span", class_="score").getText()
# print(article_upvote)

"""Finding all articles name, href,upvote"""
headings = soup.find_all(name="a", class_="storylink")
#print(headings)
all_article_texts = []
all_article_links = []

for item in headings:
    text = item.getText()
    all_article_texts.append(text)
    link = item.get("href")
    all_article_links.append(link)

#print(all_article_texts)
#print(all_article_links)

#new_list = [new_item for item in list]
#Tapping into the score class
# articles_upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]
# print(articles_upvotes)

#Splitting from 'score' string
# print(articles_upvotes[0])
# print(articles_upvotes[0].split())
# print(articles_upvotes[0].split()[0])

articles_upvotes_splitted = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
# print(articles_upvotes_splitted)

most_upvote = max(articles_upvotes_splitted)
print(most_upvote)
most_upvote_index = articles_upvotes_splitted.index(most_upvote)
# print(most_upvote_index)
most_upvote_title = all_article_texts[most_upvote_index]
print(most_upvote_title)
most_upvote_link = all_article_links[most_upvote_index]
print(most_upvote_link)