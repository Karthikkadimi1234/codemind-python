def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 1
    else:
        return 0


n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
       # print(i)
        if prime(i):
           # print(i)
            c+=1
print(c+1)