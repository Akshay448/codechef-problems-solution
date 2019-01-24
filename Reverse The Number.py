#code
t = int(input())
for i in range(t):
    n = input()
    n = n[::-1]
    n = n.lstrip('0')
    print(n)
