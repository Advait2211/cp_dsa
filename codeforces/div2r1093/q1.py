def solve():
    n = int(input())
    a = list(map(int, input().split()))


    if 67 in a:
        return "YES"
    
    return "NO"



t = int(input())
for _ in range(t):
    print(solve())