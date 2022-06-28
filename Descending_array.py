n=int(input())
a=list(map(int,input().split()))
c=sorted(a)
b=c[::-1]
if a==b:
    print("yes")
else:
    print("no")