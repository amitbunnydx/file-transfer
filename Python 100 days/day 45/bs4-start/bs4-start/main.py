from bs4 import BeautifulSoup
import requests


response=requests.get("https://news.ycombinator.com/news")
# print(response.text)

yc_web_page=response.text

soup=BeautifulSoup(yc_web_page,"html.parser")
# print(soup.title.string)
# show_name=soup.select_one(".titleline")
show_name=soup.find_all(name='a')
# print(show_name)
# for ancher in show_name:
#     print(ancher.get("href"))
#     article_text=ancher.get_text()
#     article_link=ancher.get("href")
    # print(article_text)
    # print(article_link)
article_text=[anchor.get_text() for anchor in show_name]
article_link=[anchor.get("href") for anchor in show_name]
article=soup.find_all(name="span",class_="score")
article_upvote=[int(id.getText().split()[0]) for id in article]

largest_number=max(article_upvote)
largest_index=article_upvote.index(largest_number)
print(largest_number)
print(article_text[largest_index])
print(article_link[largest_index])
# print(article)
# print(article_upvote)



#
# print(show_name)
# print(article_text)
# print(article_link)
#     print(id.getText())