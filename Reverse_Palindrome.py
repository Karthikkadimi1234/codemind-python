def palin(n):
    n=str(n)
    if n== n[::-1]:
        return 1

def reve(n):
    n=str(n)
    return int(n[::-1])
    

n=int(input())
while 1:
    n=n+reve(n)
    if palin(n):
        break
print(n)
