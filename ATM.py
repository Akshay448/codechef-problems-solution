#code
x,y = input().split()
x = int(x)
y = float(y)

if(x%5==0 and x+0.50<=y):
    z = y-x-0.50
    print('%0.2f' %z)
else:
    z = y
    print('%0.2f'%z)