n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    t=i
    rev=0
    while(i>0):
        r=i%10
        rev=rev*10+r
        i=i//10
    if t==rev:
        c+=1
print(c)
