n=int(input())
a=list(map(int,input().split()))
b=set(a)
c=set(b)
s=0
for i in c:
    s+=i
print(s)