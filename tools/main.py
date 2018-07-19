#!/usr/bin/env python
# coding:utf8
from Util import Properties 

file_path = 'test.properties'
props = Properties(file_path)   #读取文件
# props.put('key_a', 'value_a')       #修改/添加key=value
print props.get('MOBILE_EMS_Flag')            #根据key读取value
print "props.has_key('MOBILE_EMS_Flag')=" + str(props.has_key('MOBILE_EMS_Flag'))   #判断是否包含该key