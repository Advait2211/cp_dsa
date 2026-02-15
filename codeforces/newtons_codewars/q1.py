def solve():
    n = int(input())
    s = input()

    h = 0
    m = 0

    cup = 0
    cons = 0

    for c in s:
        cup /= 2
        cons += cup
        
        if c == 'M':
            cup += 0.5

        elif c == 'H':
            cup -= 0.5



    if cons > 0:
        return("M")
    elif cons < 0:
        return("H")
    else:
        return ("HM")



t = 1
for _ in range(t):
    print(solve())