from urllib import request,parse
import string
import urllib
import json
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=热门&sort=recommend&page_limit=20&page_start=0'
url = parse.quote(url,safe=string.printable)

# url1 =  parse.urlencode(url).encode('utf-8')
response = request.urlopen(url)
result = response.read().decode()
result = json.loads(result)
print(result)


