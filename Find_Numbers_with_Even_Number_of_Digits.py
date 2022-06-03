n=int(input())
d=0
a=list(map(int,input().split()))
for i in a:
    c=len(str(i))
    if(c%2==0):
        d+=1
print(d)