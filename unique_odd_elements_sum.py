n=int(input())
a=list(map(int,input().split()))
s=set(a)
k=list(s)
count=0
for i in k:
   if i%2!=0:
       count+=i
print(count)
        