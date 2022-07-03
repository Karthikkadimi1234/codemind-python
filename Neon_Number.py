n=int(input())
i=n*n
s=0
while i>0:
    r=i%10
    s+=r
    i=i//10
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")