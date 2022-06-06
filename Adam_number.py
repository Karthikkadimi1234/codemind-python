n=int(input())
rev=0
reve=0
i=n*n
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
c=rev*rev
while c>0:
    re=c%10
    reve=reve*10+re
    c=c//10
if i==reve:
    print(True)
else:
    print(False)