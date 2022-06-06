n=int(input())
i=n*n
rev=0
re=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
c=rev*rev
while c>0:
    ce=c%10
    re=re*10+ce
    c=c//10
if i==re:
    print("True")
else:
    print("False")