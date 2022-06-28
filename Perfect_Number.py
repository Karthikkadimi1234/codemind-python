n=int(input())
s=0
t=n
for i in range(1,n//2+1):
    if n%i==0:
        s+=i
if s==t:
    print(True)
else:
    print(False)