def hcf(a):
    i=1
    k=a[0]
    n=len(a)
    while(i<n):
        if a[i]%k==0:
            i+=1
        else:
            k=a[i]%k
    return k

n=int(input())
a=list(map(int,input().split()))
m=hcf(a)
print(m)
        
        