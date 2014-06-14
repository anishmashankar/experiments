from bs4 import BeautifulSoup
import urllib2
import re
seed = 'http://techieanish.blogspot.com'
visited = []
to_find = ['http://techieanish.blogspot.com']
for link in to_find:
	print 'to visit: ' + link
	try:
		page = urllib2.urlopen(link).read()
	except urllib2.HTTPError, e:
		print 'page not visited'
		visited.append((link, 'error'))
		to_find.pop(to_find.index(link))
		continue
	visited.append(link)
	print "visited: " + link
	to_find.pop(to_find.index(link))
	soup = BeautifulSoup(page)
	#print soup
	for x in soup.find_all('a',{"href":True}):
		if x['href'].endswith("html"):
			if x['href'] not in visited:
				to_find.append(x['href'])
while to_find:
	for link in to_find:
		visit(link)
print 'crawling done'