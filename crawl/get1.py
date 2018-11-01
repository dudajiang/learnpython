# -*- coding: UTF-8 -*-
from urllib import request
from urllib import parse
import chardet
import json

if __name__ == "__main__":
    # 找到network->XHR->name 中对应的那个命令，在其headers中有对应的提交地址
    RequestUrl = 'http://fy.iciba.com/ajax.php?a=fy'
    # 构建提交的Form data
    Form_Data = {}
    Form_Data['f'] = 'en'
    Form_Data['t'] = 'zh'
    Form_Data['w'] = 'river'



    data = parse.urlencode(Form_Data).encode('utf-8')
    response = request.urlopen(RequestUrl,data)
    html = response.read()
    charset = chardet.detect(html)
    html = html.decode(charset.get("encoding"))

    translate_results = json.loads(html)
    translate_results = translate_results['content']['word_mean']

    print(translate_results)
