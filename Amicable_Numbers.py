n=int(input())
m=int(input())
s=0
s1=0
for i in range(1,n//2+1):
    if n%i==0:
        s+=i
for i in range(1,m//2+1):
    if m%i==0:
        s1+=i
if s==m and s1==n:
    print("Amicable")
else:
    print("Not Amicable")