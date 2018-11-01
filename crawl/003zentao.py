# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import re
from libspider import Spider

def isLoginStatus(spider):
    url = "http://119.18.198.5:9999/zentao/index.html"
    html = spider.getUrl(url)
    soup = BeautifulSoup(html, 'lxml')
    ret = soup.find_all(text=re.compile("^self.location='/zentao/user-login-"))
    if ret:
        return False
    else:
        return True

if __name__ == "__main__":
    spider = Spider('cookie.txt')
    isLogin = isLoginStatus(spider)
    print(f"is login zentao = {isLogin}")

    if not isLogin:
        url = "http://119.18.198.5:9999/zentao/user-login.html"
        formData = {
            "account": 'dudajiang',
            "password": '123456',
        }
        spider.firstLogin(url,formData)
    
    isLogin = isLoginStatus(spider)
    print(f"is login zentao = {isLogin}")