n=int(input())
m=int(input())
sum=0
su=0
for i in range(1,n//2+1):
    if n%i==0:
        sum+=i
for j in range(1,m//2+1):
    if m%j==0:
        su+=j
if n==su and m==sum:
    print("Amicable")
else:
    print("Not Amicable")