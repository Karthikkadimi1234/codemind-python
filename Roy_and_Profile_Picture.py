lent=int(input())
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    if a<lent or b<lent:
        print("UPLOAD ANOTHER")
    if a>=lent and b>=lent:
        if a==b:
            print("ACCEPTED")
        else:
            print("CROP IT")