n=int(input())
m=int(input())
s=0
su=0
for i in range(1,n+1):
    if(n%i==0):
        s+=i
for j in range(1,m+1):
    if m%j==0:
        su+=j
if s==su:
    print("Amicable")
else:
    print("Not Amicable")