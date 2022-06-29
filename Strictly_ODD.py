n=int(input())
a=list(map(int,input().split()))
c=0
co=0
for i in range(n):
    if i%2!=0:
        if a[i]%2!=0:
            c+=1
for i in a:
    if i%2!=0:
        co+=1
if c==co:
    print(True)
else:
    print(False)
    
