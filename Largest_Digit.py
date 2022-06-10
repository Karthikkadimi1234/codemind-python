n=int(input())
s=' '
while n>0:
    r=n%10
    n=n//10
    for i in str(r):
        s+=i
print(max(s))