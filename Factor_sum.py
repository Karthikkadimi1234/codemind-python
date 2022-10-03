def fact(n):
    s=0
    for j in range(1,n+1):
        if n%j==0:
            s+=j
    return s
s=input()
a=[]
b=[]
for i in s:
    if i.isdigit():
        a.append(int(i))
for i in a:
    res=fact(i)
    if res in a:
        b.append(i)
if(b==[]):
    print(-1)
else:
    b.sort()
    for i in b:
        print(i,end=" ")
        