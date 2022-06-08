n=int(input())
t=n
c=0
while n>0:
    r=n%10
    n=n//10
    p=1
    for i in range(1,r+1):
        p*=i
    c+=p
if c==t:
    print("The number", t ,"is a strong number")
else:
    print("The number", t ,"is not a strong number")