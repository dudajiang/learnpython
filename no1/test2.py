# -*- coding: utf-8 -*-
def findMinAndMax(L):
    if len(L) == 0:
        return (None,None)
    else:
        max = min = L[0]
        for number in L:
            if number > max:
                max = number
            elif number < min:
                min = number
        return (min,max)

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')