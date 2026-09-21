import sys
input = sys.stdin.readline

def query(*args):
    print("?", *args, flush=True)
    r = int(input())
    if r == -1:
        sys.exit(0)
    return r

def answer(*args):
    print("!", *args, flush=True)

def solve():
    n = int(input())
    
    answer(u, v, d)

t = int(input())
for _ in range(t):
    solve()