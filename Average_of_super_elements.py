n=int(input())
a=list(map(int,input().split()))
b=[]
c=0
s=0
for i in a:
    if a.count(i)==i and i not in b:
        b.append(i)
for i in b:
    s+=i
    c+=1
if b==[]:
    print(-1)
else:
    d=s/c
    print("{:.2f}".format(d))
