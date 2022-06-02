a,b=map(int,input().split())
c=list(map(int,input().split()))
d=0
for i in c:
    if i<0:
        i=i*-1
    if len(str(i))==b:
        d+=1
print(d)