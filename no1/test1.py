# -*- coding: utf-8 -*-
import math  # 导入math模块，下面用到pi

list1 = [1, 9.08, 73.1]  # 将3个不同面积的圆半径定义成一个list
list2 = []


def area_sum(i):  # 定义area_sum函数，套用圆的面积计算公式
    area = math.pi * i * i
    print(area)  # 打印圆的面积
    print('index :',i)
    return area


for j in list1:  # 将列表的3个半径循环
    list2.append(area_sum(j))  # 一次将值给area_sum函数

print(list2)