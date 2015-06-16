'''
Author: Anish Mashankar
A web scraping example. Its probably a really simple demonstration
of how we can scrape HTML data from websites and play with them using
Python. Here, I have used a library called BeautifulSoup that makes
HTML parsing and reading easy.
It can be installed using pip:
pip install bs4
'''

'''
Importing necessary libraries
'''
from bs4 import BeautifulSoup #The boss. We are going to use this to parse HTML
import urllib2 #To download the web page data for extracting content
import re #simple parsing on the extracted data is done using regular expression.

a = raw_input("What do you want to know about: ") #taking a search query from user


'''
Okay, now the following step is quite important. When we see wikipedia URLs, it is
observable that the words are not separated by a space, rather, an underscore '_'.
This is what we are going to do here.
'''


c = a.replace(" ","_")


#Let's download the web page!
x = urllib2.urlopen("http://en.wikipedia.org/wiki/"+c).read()


'''
A BeautifulSoup object is initialized. It will help us wrangling the data we need
'''
soup = BeautifulSoup(x)


'''
Observing the wikipedia web page, all the content that exists in a tag
'p' inside another one called 'mw-content-text'. This is how we are going to get there.
'''


content = soup.find(id='mw-content-text') #finds the part of HTML page with content

p = content.find('p') #gets the first paragraph of the content

g = p.get_text() #gets only the text of the paragraph without the HTML elements

g = re.sub(r'\[\w+\]','', g)  #formatting off the extra tags that Wikipedia puts in for citations

print g #print the data we got
