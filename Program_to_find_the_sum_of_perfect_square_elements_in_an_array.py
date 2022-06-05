import math
n=int(input())
a=list(map(int,input().split()))
s=0
b=[]
for i in a:
    c=int(math.sqrt(i))
    if(c*c==i):
        b.append(i)
for i in b:
    s+=i
print(s)