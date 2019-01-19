#code
n = int(input())
winner = 0
lead = 0
max_lead = 0
player1 = player2 = 0
for i in range(n):
    a,b = map(int, input().split())
    player1+=a
    player2+=b
    lead = abs(player1-player2)
    if(lead>max_lead):
        max_lead = lead
        if(player1>player2):
            winner = 1
        else:
            winner = 2
print(winner,max_lead)            
