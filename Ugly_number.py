def prime(n):
    if n>1:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return 0
        else:
            return 1
        
n=int(input())
#print(n)
c=0
d=[]
for i in range(1,n//2+1):
    if n%i==0:
        if prime(i):
            d.append(i)
#print(d)
for i in d:
    if i<=5:
        c=1
    else:
        c=0
        break
if c==1 or n==1:
    print("Ugly Number")
else:
    print("Not Ugly Number")
