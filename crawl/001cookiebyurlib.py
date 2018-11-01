# -*- coding: UTF-8 -*-
from urllib import request
from urllib import parse
from http import cookiejar
from bs4 import BeautifulSoup
import chardet
import json
import re

# 和利用cookie进行登录相关的代码样例


def myRequest():
    userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    header = [('User-Agent', userAgent),
              ('Referer', 'http://119.18.198.5:9999/zentao/my/'),
              ('Connection', 'keep-alive')]
    filename = 'cookie.txt'
    cookie = cookiejar.MozillaCookieJar(filename)
    cookie.load(filename, ignore_discard=True, ignore_expires=True)
    # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
    handler = request.HTTPCookieProcessor(cookie)
    # 通过CookieHandler创建opener
    opener = request.build_opener(handler)
    opener.addheaders = header
    request.install_opener(opener)
    return {'request': request, 'cookie': cookie}


def firstLogin(account, password):
    # 马蜂窝模仿 登录
    print("开始模拟登录禅道")

    loginUrl = "http://119.18.198.5:9999/zentao/user-login.html"

    myreq = myRequest()
    print(myreq['cookie'])

    formData = {
        "account": account,
        "password": password,
    }
    data = parse.urlencode(formData).encode('utf-8')

    response = myreq['request'].urlopen(loginUrl, data)
    myreq['cookie'].save(ignore_discard=True, ignore_expires=True)
    # 打印cookie信息
    for item in myreq['cookie']:
        print('Name = %s' % item.name)
        print('Value = %s' % item.value)

    # 无论是否登录成功，状态码一般都是 statusCode = 200
    html = response.read()
    charset = chardet.detect(html)
    html = html.decode(charset.get("encoding"))
    print(html)


def isLoginStatus():
    routeUrl = "http://119.18.198.5:9999/zentao/index.html"
    myreq = myRequest()
    response = myreq['request'].urlopen(routeUrl)
    html = response.read()
    charset = chardet.detect(html)
    html = html.decode(charset.get("encoding"))
    # print(html)
    soup = BeautifulSoup(html, 'lxml')

    ret = soup.find_all(text=re.compile("^self.location='/zentao/user-login-"))
    if ret:
        return False
    else:
        return True

def getTaskStatus():
    routeUrl = "http://119.18.198.5:9999/zentao/company-dynamic-today--date_desc-381-2000-1.html"
    myreq = myRequest()
    response = myreq['request'].urlopen(routeUrl)
    # myreq['cookie'].save(ignore_discard=True, ignore_expires=True)

    # myreq = myRequest()
    # for item in myreq['cookie']:
    #     print('Name = %s' % item.name)
    #     print('Value = %s' % item.value)

    html = response.read()
    charset = chardet.detect(html)
    html = html.decode(charset.get("encoding"))
    # print(html)
    soup = BeautifulSoup(html, 'lxml')
    souptbody = BeautifulSoup(str(soup.tbody.contents),'lxml')
    souptrlist = souptbody.find_all(class_='text-center')
    # print(souptrlist)
    i=0
    for child in souptrlist:
        i = i+1
        print(i)
        aa = child.contents
        print(aa)
        if i>10:
            break
        # print(aa[1].string,aa[3].string,aa[5].string,aa[7].string,aa[9].string)
        # for tdchild in child.children:
        #     print(tdchild.string)



if __name__ == "__main__":
    isLogin = isLoginStatus()
    print(f"is login zentao = {isLogin}")

    if not isLogin:
        firstLogin('dudajiang', '123456')
    
    getTaskStatus()



