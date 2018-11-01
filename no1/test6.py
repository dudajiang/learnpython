import math

num = []

for i in range(899):
  j = 100 + i
  bai = str(j)[0]
  shi = str(j)[1]
  ge = str(j)[2]
  if (bai!=shi and bai!=ge and shi!=ge and int(bai)>0 and int(shi)>0 and int(ge)>0):
    print(int(j))
    num.append(j)

sum = 0
for i in num:
  sum = sum + i
print(len(num))
print(sum)
    