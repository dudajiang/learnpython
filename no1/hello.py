# -*- coding: utf-8 -*-
a = '杜沛渔是个好姑娘'
b = a
a = 'Hi, %s, you have $%d.' % ('Michael', 1000000)
print(b)
print(a)
print(b)

s1 = 72
s2 = 85
r  = (s2-s1)/s1*100

print ('小明的成绩提高了：%f %%' %r)

n=input('what\'s your name:')
s1=input('请输入去年的成绩：')
s2=input('请输入今年的成绩：')
t=(float(s2)-float(s1))/float(s1)*100
if t>0 :
    print('恭喜%s,你的成绩提高了%.3f%%' %(n,t))
else :
    t=abs(t)
    print('很遗憾%s,你的成绩降低了%.1f%%' %(n,t))

