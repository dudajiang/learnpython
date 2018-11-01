# -*- coding: UTF-8 -*-
from urllib import request
from urllib import parse
import chardet
import json


userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'


def myLogin(account, password):
    # 马蜂窝模仿 登录
    print("开始模拟登录")

    RequestUrl = 'https://passport.mafengwo.cn/login/'

    header = {
        "Referer": "https://passport.mafengwo.cn/",
        'User-Agent': userAgent,
    }

    Form_Data = {
        "passport": account,
        "password": password,
    }
    data = parse.urlencode(Form_Data).encode('utf-8')

    req = request.Request(RequestUrl, headers=header)
    response = request.urlopen(req, data)

    # 无论是否登录成功，状态码一般都是 statusCode = 200
    html = response.read()
    charset = chardet.detect(html)
    html = html.decode(charset.get("encoding"))
    print(html)


if __name__ == "__main__":
    myLogin("dudajiang", "123456")
    # 找到network->XHR->name 中对应的那个命令，在其headers中有对应的提交地址

    # html = response.read()
    # charset = chardet.detect(html)
    # html = html.decode(charset.get("encoding"))
    # print(html)
