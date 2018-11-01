# -*- coding: UTF-8 -*-
from urllib import request
from urllib import parse
from http import cookiejar
from bs4 import BeautifulSoup
import chardet
import json
import re
import time
import random
import os
import traceback


class Spider:
    def __init__(self, filename=''):
        userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
        headers = [('User-Agent', userAgent),
                   ('Connection', 'keep-alive')]
        cookie = None
        if filename:
            cookie = cookiejar.MozillaCookieJar(filename)
            cookie.load(filename, ignore_discard=True, ignore_expires=True)
            handler = request.HTTPCookieProcessor(cookie)
        else:
            handler = request.HTTPHandler()
        opener = request.build_opener(handler)
        opener.addheaders = headers
        request.install_opener(opener)
        self.request = request
        self.cookies = cookie

    def firstLogin(self, url, data):
        print("开始模拟登录:", url)
        data = parse.urlencode(data).encode('utf-8')
        response = self.request.urlopen(url, data)
        self.cookies.save(ignore_discard=True, ignore_expires=True)
        # 打印cookie信息
        # for item in myreq['cookie']:
        #     print('Name = %s' % item.name)
        #     print('Value = %s' % item.value)
        # 无论是否登录成功，状态码一般都是 statusCode = 200
        html = response.read()
        charset = chardet.detect(html)
        html = html.decode(charset.get("encoding"))
        # print(html)

    def getUrl(self, url, data=None):
        """页面请求方法"""
        # 请求页面方法
        MaxTryTimes = 20
        waite_time = random.uniform(0, 1)  # 初始化等待时间
        for i in range(MaxTryTimes):
            time.sleep(waite_time)
            if data:
                data = parse.urlencode(data).encode('utf-8')
            response = self.request.urlopen(url, data)
            html = response.read()
            charset = chardet.detect(html)
            html = html.decode(charset.get("encoding"))
            break
            # print(html)
            # try:
            #     data = parse.urlencode(data).encode('utf-8')
            #     response = self.request.urlopen(url, data)
            #     html = response.read()
            #     charset = chardet.detect(html)
            #     html = html.decode(charset.get("encoding"))
            #     print(html)
            #     break
            # except Exception as e:
            #     print(e)
            #     html = ''
        return html

    def saveFileByUrl(self, url, dirname=None, filename=None):
        """页面请求方法"""
        #
        try:
            if (filename == None):
                filename = url.split('/')[-1]
            if (dirname == None):
                dirname = '/Users/shirly/ddj/temp/printfile'
            print(filename)
            print(dirname)
            path = dirname+'/'+filename
            data = self.request.urlopen(url)
            if not os.path.exists(dirname):
                os.makedirs(dirname)
            with open(path, 'wb') as f:
                f.write(data.read())
                f.close()
                print(path+' 文件保存成功')
        except Exception as identifier:
            traceback.print_exc()
