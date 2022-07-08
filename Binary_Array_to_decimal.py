n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    s+=i*10**(n-1)
    n-=1
s=str(s)
s=s[::-1]
su=0
j=0
for i in s:
    su+=int(i)*2**j
    j+=1
print(su)
    