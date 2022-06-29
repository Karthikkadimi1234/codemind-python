n=int(input())
a=list(map(int,input().split()))
b=a[::-1]
ind=0
for i in range(n):
    if b[i]%2==0:
        if i==0:
            ind=n-1
            break
        else:
            ind=n-i-1
            break
print(ind)    
