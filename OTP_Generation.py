n=input()
a=int(n)
s=''
rev=0
while a>0:
    t=a%10
    rev=rev*10+t
    a=a//10
while rev>0:
    r=rev%10
    rev=rev//10
    c=str(r)
    for i in c:
        d=int(i)
        if d%2!=0:
            s+=str(d*d)
print(s)
    
        