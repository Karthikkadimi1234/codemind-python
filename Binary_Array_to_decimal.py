n=int(input())
a=list(map(int,input().split()))
b=a[::-1]
s,j=0,0
for i in b:
        s+=i*2**j
        j+=1
        
print(s)
    