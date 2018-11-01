# -*- coding: UTF-8 -*-
userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'

header = [('User-Agent', userAgent),
          ('Referer', 'http://119.18.198.5:9999/zentao/my/'),
          ('Connection', 'keep-alive')]
for x in header:
    print(x)
