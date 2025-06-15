def solve():
    w, h, a, b = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())

    x_gap = abs(x2 - x1)
    y_gap = abs(y2 - y1)

    if x_gap == 0:
        if y_gap % b == 0:
            return "Yes"
        else:
            return "No"
    
    if y_gap == 0:
        if x_gap % a == 0:
            return "Yes"
        else:
            return "No"


    if x_gap % a == 0:
        return "Yes"

    if y_gap % b == 0:
        return "Yes"

    return "No"
    
    
    

    



t = int(input())

for _ in range(t):
    print(solve())