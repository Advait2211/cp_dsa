def solve():
    n = int(input())
    a = list(map(int, input().split()))

    if 0 not in a:
        return 'NO'
    
    if len(set(a)) == 1:
        return "NO"

    zeros = a.count(0)

    if zeros > 1:
        if 1 not in a:
            return "NO"
        
    
    return "YES"



t = int(input())
for _ in range(t):
    print(solve())