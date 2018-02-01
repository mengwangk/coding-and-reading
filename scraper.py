import urllib.request

# https://docs.python.org/3/howto/urllib2.html
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
with urllib.request.urlopen('https://www.python.org/') as response:
   html = response.read()
   print(html)
