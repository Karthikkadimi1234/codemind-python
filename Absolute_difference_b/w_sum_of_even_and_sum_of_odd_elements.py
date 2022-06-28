n=int(input())
a=list(map(int,input().split()))
s=0
su=0
for i in a:
    if i%2==0:
        s+=i
    else:
        su+=i
print(abs(s-su))