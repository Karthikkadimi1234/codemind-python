n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    rev=0
    while i>0:
        r=i%10
        rev=rev*10+r
        i=i//10
    b.append(rev)
print(*b)