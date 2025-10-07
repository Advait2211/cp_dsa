def solve():
    n = int(input())
    a = list(map(int, input().split()))
    total = 0
    negs = 0

    for ele in a:
        if ele == 0:
            total += 1
        elif ele == -1:
            negs += 1
            
    if negs % 2 == 1:
        return total + 2
    
    return total




t = int(input())
for _ in range(t):
    print(solve())