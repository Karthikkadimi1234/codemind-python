n=int(input())
arr=list(map(int,input().split()))
m=arr[0]
j=1
while(j<n):
    if(arr[j]%m==0):
        j+=1
    else:
        m=arr[j]%m
print(m)
       
       

    