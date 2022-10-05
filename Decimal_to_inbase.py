n=int(input())
m=int(input())
b=[]
while n>=1:
    r=n%m
    b.append(r)
    n=n//m
c=0
d=[]
for i in b:
    if i==0:
        c+=1
    else:
        d.append(c)
        e=c
        c=0
f=0
for i in b:
    if i==0:
        f+=1
if f==0:
    print(-1)
else:
    print(max(d))

        