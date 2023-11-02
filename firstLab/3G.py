t = int(input())
counter = 0
games = []
while counter < t:
    games.append([int(i) for i in input().split()])
    counter+=1

for i in range(len(games)):
    imposters = games[i][0]
    crewmates = games[i][1]
    rounds=0
    while imposters > 0 and crewmates > 0:
        crewmates -= imposters
        if crewmates <= 0:
            rounds += 1
            break
        imposters-=1
        rounds+=1
    if imposters <= 0:
        print("Crewmates")
        print(rounds)
    else:
        print("Impostors")
        print(rounds)