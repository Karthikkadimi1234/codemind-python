n=int(input())
a=list(map(int,input().split()))
c=[]
for i in a:
   re=0
   while(i>0):
       r=i%10
       re=re*10+r
       i=i//10
   c.append(re)
print(*c)
