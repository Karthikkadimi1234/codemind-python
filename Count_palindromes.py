n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    t=i
    re=0
    while(i>0):
        r=i%10
        re=re*10+r
        i=i//10
    if re==t:
        c+=1
print(c)
    