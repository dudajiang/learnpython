# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import re
from libspider import Spider
import pypinyin
import string
import pandas as pd
from pandas import Series, DataFrame

spider = Spider()
pages = {
    'titlecn': [],
    'titlepy': [],
    'url': []
}

imgs = {
    'titlecn': [],
    'titlepy': [],
    'num': [],
    'url': [],
    'imgurl': []
}


def hp(word):
    s = ''
    for i in pypinyin.pinyin(word, style=pypinyin.NORMAL):
        s += ''.join(i)
    return s


def getListPage():
    url = "http://bj.aoshu.com/e/20171215/5a336e1fc9928.shtml"
    html = spider.getUrl(url)
    # print(html)
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup)
    souptrlist = soup.find_all('a', string=re.compile("真题（"))
    i = 0
    for child in souptrlist:
        i = i+1
        # print(i)
        # print(child.get('href'))
        aa = child.span.contents[0]
        aa = aa.translate(aa.maketrans('', '', '（）'))
        bb = hp(aa)
        # print(bb)
        pages['titlecn'].append(aa)
        pages['titlepy'].append(bb)
        pages['url'].append(child.get('href'))
    frame1 = DataFrame(pages)
    return frame1


def getDetailImg(url):
    html = spider.getUrl(url)
    soup = BeautifulSoup(html, 'html.parser')
    soup1 = soup.find('div', class_="btn-pages")
    soupimg = soup1.find_previous("img")
    return soupimg.get('src')


def getImgName():
    filename = imgs['titlepy'][-1]
    num = imgs['num'][-1]
    filename += '_'+str(num)+'.png'
    return filename


def getDetailPage(row):
    url = row['url']
    i = 1

    html = spider.getUrl(url)
    # print(html)
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup)
    # soup2 = soup.find_all('img', alt='', src=re.compile('png$'))
    soup1 = soup.find('div', class_="btn-pages")
    soup2 = soup1.find_all('a', href=re.compile("html$"))
    soupimg = soup1.find_previous("img")
    imgs['titlecn'].append(row['titlecn'])
    imgs['titlepy'].append(row['titlepy'])
    imgs['num'].append(i)
    imgs['url'].append(row['url'])
    imgs['imgurl'].append(soupimg.get('src'))
    print(getImgName())
    print(imgs['imgurl'][-1])
    spider.saveFileByUrl(imgs['imgurl'][-1], filename=getImgName())
    for index in range(len(soup2)-1):
        child = soup2[index]
        i = i+1
        imgs['titlecn'].append(row['titlecn'])
        imgs['titlepy'].append(row['titlepy'])
        imgs['num'].append(i)
        imgs['url'].append(child.get('href'))
        aa = getDetailImg(child.get('href'))
        imgs['imgurl'].append(aa)
        print(getImgName())
        spider.saveFileByUrl(imgs['imgurl'][-1], filename=getImgName())
        print(aa)
    print(len(imgs['titlecn']))


def test():
    url = 'http://files.eduuu.com/img/2017/12/15/104832_5a3338006770c.png'
    spider.saveFileByUrl(url, filename='aa.png', dirname='./ddj')


if __name__ == "__main__":
    pageframe = getListPage()
    for index, row in pageframe.iterrows():
        getDetailPage(row)
