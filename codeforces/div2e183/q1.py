def solve():
    n = int(input())
    
    k = n % 3

    if k == 0:
        return k
    else:
        return 3 - k



t = int(input())
for _ in range(t):
    print(solve())