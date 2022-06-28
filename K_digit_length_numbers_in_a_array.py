n,k=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in a:
    if i<0:
        i=i*-1
        if k==len(str(i)):
            c+=1
    else:
         if k==len(str(i)):
            c+=1
print(c)