n=int(input())
a=list(map(int,input().split()))
se=int(input())
f=0
for i in a:
    if i==se:
        f=1
if f==1:
    print(True)
else:
    print(False)
        
