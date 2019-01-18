#code

def calculate_sum(N):
    sum = 0
    while(N!=0):
        sum += N%10
        N = N//10
    return sum    

t = int(input())

for i in range(t):
    N = int(input())
    print(calculate_sum(N))
