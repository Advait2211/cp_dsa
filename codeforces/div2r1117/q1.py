import sys
input = sys.stdin.readline

def solve():
    w, a = map(int, input().split())

    words = set()
    abbs = set()

    exit = False

    for _ in range(w):
        ip = input().strip()
        ip = ip[0].upper()
        words.add(ip)

    for _ in range(a):
        ip = input().strip()

        for char in ip:
            if char not in words:
                exit = True

        words.add(ip)

    if exit == True:
        return "NO"
    return "YES"


    


t = int(input())
for _ in range(t):
    print(solve()) 