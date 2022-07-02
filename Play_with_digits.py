n=int(input())
a=list(map(int,input().split()))
s=0
b=[]
for i in a:
    while i>0:
        r=i%10
        s+=r
        i=i//10
print(s)