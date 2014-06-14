from bs4 import BeautifulSoup
import urllib2
import re
a = raw_input("What do you want to know about: ")
c = a.replace(" ","_")
x = urllib2.urlopen("http://en.wikipedia.org/wiki/"+c).read()
soup = BeautifulSoup(x)
content = soup.find(id='mw-content-text')
p = content.find('p')
g = p.get_text()
g = re.sub(r'\[\w+\]','', g)
print g