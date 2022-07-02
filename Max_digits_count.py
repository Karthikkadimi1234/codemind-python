n=int(input())
a=list(map(int,input().split()))
d=0
b=[]
for i in a:
    c=len(str(i))
    b.append(c)
for i in b:
    if max(b)==i:
        d+=1
print(d)