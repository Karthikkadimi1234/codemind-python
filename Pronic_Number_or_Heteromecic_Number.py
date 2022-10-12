n=int(input())
c=0
for i in range(1,n//2+1):
    for j in range(1,n//2+1):
        if i*j==n and abs(i-j)==1:
            c=1
if c==1:
    print("YES")
else:
    print("NO")