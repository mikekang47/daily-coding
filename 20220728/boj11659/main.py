import sys
s=lambda:map(int,sys.stdin.readline().split())
n,m=s()
a=[0]
for i in s(): a+=[a[-1]+i]
for i in range(m): x,y=s(); print(a[y]-a[x-1])