n=int(input())
a=list(map(int,input().split()))
b=set(a)
c=list(b)
s=0
for i in c:
    if c.count(i)==1:
        s+=i
print(s)