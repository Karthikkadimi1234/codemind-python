n=int(input())
a=list(map(int,input().split()))
b=[]
d=0
for i in a:
    c=len(str(i))
    b.append(c)
for i in b:
    if min(b)==i:
        d+=1
print(d)