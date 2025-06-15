import math

def solve():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    
    arr = []
    teams = 0

    for num in a:
        if num >= x:
            teams += 1
        else:
            arr.append(num)
    
    arr.sort(reverse=True)
    team_size = 0

    
    for p in arr:
        team_size += 1
        if team_size * p >= x:
            teams += 1
            team_size = 0
            
    return teams


    

t = int(input())

for _ in range(t):
    print(solve())
