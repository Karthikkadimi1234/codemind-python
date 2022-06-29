n=int(input())
a=list(map(int,input().split()))
b=set(a)
c=set(b)
d=0
for i in c:
    if i%2!=0:
        d+=1
print(d)