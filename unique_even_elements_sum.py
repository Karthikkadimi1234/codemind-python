n=int(input())
a=list(map(int,input().split()))
b=set(a)
c=list(b)
s=0
for i in c:
    if i%2==0:
        s+=i
print(s)