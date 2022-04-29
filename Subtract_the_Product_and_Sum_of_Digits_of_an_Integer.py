n=int(input())
su=0
pro=1
while n>0:
    r=n%10
    n=n//10
    su+=r
    pro*=r
print(pro-su)