t = int(input())
numbers = []
for i in range(t):
    num = int(input())
    numbers.append(num)

numbers.sort()    
for i in range(t):
    print(numbers[i])
