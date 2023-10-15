from bs4 import BeautifulSoup
import requests

link = "https://www.cbc.ca/news"
data = requests.get(link)

data

soup = BeautifulSoup(data.text, "html.parser")


news = soup.find_all('a',attrs={'class':'card'}, limit=9)

print("top 10 news stories on cbc:\n")

top_news = soup.find('a', attrs= {'class': 'primaryHeadlineLink'})
print(top_news.h3.text)
print("https://www.cbc.ca" + top_news['href'], "\n")

for story in news:
  print(story.h3.text)
  print("https://www.cbc.ca" + story['href'], "\n")