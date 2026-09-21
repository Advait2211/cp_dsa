import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = input().strip()

    if n % 2 == 1:
        return "NO"
    
    op = 0
    cl = 0

    for char in a:
        # print(char)
        if char == '(':
            op += 1
        else:
            cl += 1

    if op == cl:
        return "YES"
    else:
        return 'NO'
    


t = int(input())
for _ in range(t):
    print(solve()) 