import feedparser
import time
from os import system
NewsFeed = feedparser.parse("http://xml2.corriereobjects.it/rss/homepage.xml")

print("Number of  RSS post: ", len(NewsFeed.entries))

for n, entry in enumerate(NewsFeed.entries):
  for j in ("Ukraina", "Russia", "Zelensky", "Draghi", "Guerra", "Putin"):
    if j.lower() in entry.title.lower():
      a = str(entry.title)
      b = len(a)
      c = 0
      d = 20
      while d < b:
          print(a[c:d])
          c += 1
          d += 1
          system('clear')
          time.sleep(0.125)
      print(entry.title)

print("\n\n------------")


print(New)
