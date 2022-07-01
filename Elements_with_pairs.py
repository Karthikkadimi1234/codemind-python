n=int(input())
a=list(map(int,input().split()))
c=0
for i in  a:
    c+=1
if c%2==0:
    print(*a)
else:
    a.append(0)
    print(*a)
    