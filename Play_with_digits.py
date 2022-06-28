n=int(input())
a=list(map(int,input().split()))
c=[]
s=0
su=0
for i in a:
#    s=0
    while(i>0):
        r=i%10
        s+=r
        i//=10
print(s)
#    c.append(s)
#for i in c:
#   su+=i
#print(su)