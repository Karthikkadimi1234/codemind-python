import math
a,b=map(int,input().split())
c=0
n=a
v=a % pow(10,b)
while a>=pow(10,b) :
    a=a//10
print(abs(v-a))
    