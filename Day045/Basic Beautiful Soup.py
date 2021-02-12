
"""#Basic Beautiful Soup"""
from bs4 import BeautifulSoup
#import lxml

with open("website.html", encoding="utf8") as file:
    data = file.read()

soup = BeautifulSoup(data, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
#
# print(soup)
# print(soup.prettify())
#
# print(soup.a)
# print(soup.li)
# print(soup.p)

"""#Finding all the anchor tags"""
all_anchor_tags = soup.find_all(name="a")
#print(all_anchor_tags)

"""#Finding all the paragraph tags"""
all_parahraph_tags = soup.find_all(name="p")
#print(all_parahraph_tags)

"""#Printing all the texts from anchor tags"""
for tag in all_anchor_tags:
    tag_text = tag.getText()
    # print(tag_text) #printing the texts
    href = tag.get("href")
    #print(href)

"""#Finding all value from attribute"""

heading = soup.find_all(name="h1")
#print(heading)

"""##Finding a specific value from id attribute"""
heading_h1 = soup.find_all(name="h1", id="name")
#print(heading_h1)

"""##Finding a specific value from class attribute"""
#Uses class_ to avoid error occuring for Class
section_heading = soup.find(name="h3", class_="heading")
# print(section_heading) #prints the whole section heading
# print(section_heading.getText()) #Prints text
# print(section_heading.name) #prints name of the tag
# print(section_heading.get("class")) #prints the class name

"""#finding a tag inside another tag"""

#Company url is an anchor tag which is in a paragraph using css selector
company_url = soup.select_one(selector="p a")
print(company_url)

#Finding name by using id
name = soup.select_one(selector="#name")
print(name)

#Finding all headings by using class

headings = soup.select(selector=".heading")
print(headings)

#Finding the first heading by using class

headings = soup.select_one(selector=".heading")
print(headings)