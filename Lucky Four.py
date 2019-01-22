#code
t = int(input())
for i in range(t):
    count = 0
    n = input()
    for j in range(len(n)):
        if(n[j]=='4'):
            count+=1
    print(count)    
