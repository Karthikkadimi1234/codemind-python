a=input()
a=a.split(' ')
b=list(a)
s=0
sm=0
for i in b:
    m=min(i)
    ma=max(i)
    s+=ord(m)
    sm+=ord(ma)
print(abs(s-sm))