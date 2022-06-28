n=int(input())
a=list(map(int,input().split()))
s=0
su=0
for i in range(n):
    if i%2==0:
        s+=a[i]
    else:
        su+=a[i]
print(abs(s-su))