n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
for i in range(n//2,n):
    b.append(a[i])
d=b[::-1]
for i in d:
    c.append(i)
for i in range(n//2):
    c.append(a[i])
print(*c)