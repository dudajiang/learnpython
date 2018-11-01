#--coding:utf-8
# 加载库
import urllib
import json
import string
from bs4 import BeautifulSoup

# 获取所有标签
url = 'https://movie.douban.com/j/search_tags?type=movie'
request = urllib.request.Request(url=url)
response = urllib.request.urlopen(request, timeout=20)
result = response.read()
# 加载json为字典
result = json.loads(result)
tags = result['tags']

print(tags)

# 定义一个列表存储电影的基本信息
movies = []
# 处理每个tag
for tag in tags:
	start = 0
	# 不断请求，直到返回结果为空
	while 1:
		# 拼接需要请求的链接，包括标签和开始编号
		url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=' + tag + '&sort=recommend&page_limit=20&page_start=' + str(start)
		url = urllib.parse.quote(url,safe=string.printable)
        # url1 = urllib.parse.unquote(url)
		request = urllib.request.Request(url)
		response = urllib.request.urlopen(request, timeout=20)
		result = response.read()
		result = json.loads(result)

		# 先在浏览器中访问一下API，观察返回json的结构
		# 然后在Python中取出需要的值 
		result = result['subjects']

		# 返回结果为空，说明已经没有数据了
		# 完成一个标签的处理，退出循环
		if len(result) == 0:
			break

		# 将每一条数据都加入movies
		for item in result:
			movies.append(item)
		
		start += 20
		# break
	break

		# 使用循环记得修改条件
		# 这里需要修改start
		

# 看看一共获取了多少电影
print(len(movies))