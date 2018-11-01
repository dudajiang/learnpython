# -*- coding: UTF-8 -*-
from urllib import request
from urllib import parse
import chardet
import json
from bs4 import BeautifulSoup
import re

if __name__ == "__main__":
    # 找到network->XHR->name 中对应的那个命令，在其headers中有对应的提交地址
    RequestUrl = 'https://ipn.boco.com.cn'
    # proxy = {'http':'14.118.232.24:10010'}
    # proxy_support = request.ProxyHandler(proxy)
    # opener = request.build_opener(proxy_support)
    # opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    # request.install_opener(opener)
    # response = request.urlopen(RequestUrl)

    head={}
    head['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    req = request.Request(RequestUrl, headers=head)
    response = request.urlopen(req)
    
    html = response.read()
    charset = chardet.detect(html)
    html = html.decode(charset.get("encoding"))

    # print(html)
    soup = BeautifulSoup(html,'lxml')
    print(soup.prettify())
    
    # print(soup.find_all(text=re.compile("^self.location='/zentao/user-login-")))
    # print(response.getcode())