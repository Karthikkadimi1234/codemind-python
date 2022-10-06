def sel(n):
    t=n
    c=0
    while(n>0):
        r=n%10
        n=n//10
        if r!=0 and t%r==0:
            c+=1
    if c==len(str(t)):
        return 1
            
n=int(input())
m=int(input())
for i in range(n,m+1):
    if sel(i):
        print(i,end=" ")