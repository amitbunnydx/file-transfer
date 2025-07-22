from tkinter.font import names

from bs4 import BeautifulSoup
import lxml


with open("website.html",'r') as file:
    content=file.read()
    # print(content)

soup=BeautifulSoup(content, "html.parser")

# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.a)

all_anchor_tag=soup.find_all(name="a")
# print(all_anchor_tag)
for tags in all_anchor_tag:
    pass
    # print(tags.getText())
    # print(tags.get("href"))

# heading=soup.find(name="h1",id="name")
# print(heading)
#
# selection_heading=soup.find(name="h3",class_="heading")
# print(selection_heading.get_text())
# print(selection_heading.get("class"))




