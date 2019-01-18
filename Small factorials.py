#code
t = int(input())

def fact(n):
    if(n==0 or n==1):
        return 1
    return n*fact(n-1)    

for i in range(t):
    n = int(input())
    print(fact(n))
