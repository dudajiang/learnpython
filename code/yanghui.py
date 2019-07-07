num = 11
LL = [[1]]
print(LL)

for i in range(1,num):
  LL.append([(0 if j== 0 else LL[i-1][j-1])+ (0 if j ==len(LL[i-1]) else LL[i-1][j]) for j in range(i+1)])

for i in range(num,2*num-1):
  k = 2*num-1-i
  LL.append([(LL[i-1][j-1]+ LL[i-1][j]) for j in range(1,k+1)])

print(LL)