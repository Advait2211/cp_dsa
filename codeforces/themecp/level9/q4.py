# https://codeforces.com/contest/1759/problem/C

"""
logic: there are only 5 possible answers
0 if a == b
-1 if b cannot be reached
 
1 if b can directly be reached from a
2 if 'a' can reach to one end, and then do a reversal to 'b'
3 otherwise (the gap is sufficient to make it work)
"""
 
 
 
def solve():
    l, r, x = map(int, input().split())
    a, b = map(int, input().split())
 
 
    if a == b:
        return 0
    
    if a + x > r and a - x < l:
        return -1
 
    if a > b:
        if a - x >= b:
            return 1
 
        # 0 15 5
        # 3 7
        # 3 - 15 - 7
 
        # 0 10 5
        # 3 7
        # 3 - 10 - 2 - 7
        
    elif a < b:
        if a + x <= b:
            return 1
 
    if l + x > b and r - x < b:
        return -1
 
    if r - a >= x:
        if r - b >= x:
            return 2
        
    if a - l >= x:
        if b - l >= x:
            return 2
        
 
    return 3
 
 
 
 
 
t = int(input())
 
for _ in range(t):
    print(solve())