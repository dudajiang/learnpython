# -*- coding: UTF-8 -*-
from http import cookiejar
from bs4 import BeautifulSoup
import requests
import chardet
import json
import re

# 和利用cookie进行登录相关的代码样例


def getHeader():
    userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    header = {
        'User-Agent': userAgent,
        'Referer': 'http://119.18.198.5:9999/zentao/my/',
        'Connection': 'keep-alive'
    }
    return header


def getSession():
    filename = 'cookiebyrequest.txt'
    mySession = requests.session()
    mySession.cookies = cookiejar.MozillaCookieJar(filename=filename)
    try:
        mySession.cookies.load(filename, ignore_discard=True, ignore_expires=True)
    except:
        print('未找到cookies文件')
    return mySession


def firstLogin(account, password):
    print("开始模拟登录禅道")

    loginUrl = "http://119.18.198.5:9999/zentao/user-login.html"

    mySession = getSession()
    headers = getHeader()
    # print(mySession)

    formData = {
        "account": account,
        "password": password,
    }

    response = mySession.post(loginUrl,data=formData,headers=headers)
    mySession.cookies.save(ignore_discard=True, ignore_expires=True)
    html = response.text
    print(html)
    # 打印cookie信息
    for item in mySession.cookies:
        print('Name = %s' % item.name)
        print('Value = %s' % item.value)

def isLoginStatus():
    routeUrl = "http://119.18.198.5:9999/zentao/index.html"
    mySession = getSession()
    headers = getHeader()
    response = mySession.get(routeUrl,headers=headers)
    # if response.status_code != 200:
    #     return False
    # else:
    #     return True
    html = response.text
    print(html)
    soup = BeautifulSoup(html, 'lxml')

    ret = soup.find_all(text=re.compile("^self.location='/zentao/user-login-"))
    if ret:
        return False
    else:
        return True

def getTaskStatus():
    routeUrl = "http://119.18.198.5:9999/zentao/company-dynamic-today--date_desc-381-2000-1.html"
    mySession = getSession()
    headers = getHeader()
    response = mySession.get(routeUrl,headers=headers)

    html = response.text
    print(response.encoding)
    html = html.encode(response.encoding).decode()
    print(html)
    # soup = BeautifulSoup(html, 'lxml')
    # souptbody = BeautifulSoup(str(soup.tbody.contents),'lxml')
    # souptrlist = souptbody.find_all(class_='text-center')
    # # print(souptrlist)
    # i=0
    # for child in souptrlist:
    #     i = i+1
    #     print(i)
    #     aa = child.contents
    #     print(aa[1].string,aa[3].string,aa[5].string,aa[7].string,aa[9].string)
        # for tdchild in child.children:
        #     print(tdchild.string)



if __name__ == "__main__":
    # firstLogin('dudajiang', '123456')
    isLogin = isLoginStatus()
    print(f"is login zentao = {isLogin}")

    if not isLogin:
        firstLogin('dudajiang', '123456')
    
    getTaskStatus()



