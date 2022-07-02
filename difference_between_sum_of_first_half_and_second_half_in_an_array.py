n=int(input())
a=list(map(int,input().split()))
s=0
s1=0
for  i in range(n//2+1):
    s+=i
for i in range(n//2+1,n+1):
    s1+=i
print(abs(s-s1))