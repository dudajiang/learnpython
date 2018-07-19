#!/usr/bin/env python
# coding:utf8

import shutil
import os

source = '/Users/shirly/ddj/temp/联通/河南/test/syscfg-db.properties'
target = '/Users/shirly/ddj/temp/联通/广东/test/syscfg-db.properties'
path=os.path.split(target)
print path[0]
# shutil.copy2(source,target)
