n=int(input())
temp=n
re=0
while n!=0:
    r=n%10
    re=re*10+r
    n=n//10
if re==temp:
    print("True")
else:
    print("False")
