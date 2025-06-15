def solve():
    w, h, a, b = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())

    x_stat = True

    # # check if overlap
    # if max(x1, x2) <= min(x1 + b, x2 + b):
    #     # gap in between
    #     gap = max(x2 - (x1+b), x1 - (x2 + b))

    #     if gap % a != 0:
    #         x_no = False
    #     else:
    #         return "Yes"
        
    #     gap = max(y2 - (y1+a), y1 - (y2 + a))

    #     if gap % b == 0:
    #         return "Yes"
    #     else:
    #         if x_no == False:
    #             return "No"
    #         else:
    #             return "Yes"

    # elif max(y1, y2) <= min(y1 + a, y2 + a):
    #     gap = max(x2 - (x1+b), x1 - (x2 + b))

    #     if gap % a != 0:
    #         x_no = False
    #     else:
    #         return "Yes"
        
    #     gap = max(y2 - (y1+a), y1 - (y2 + a))

    #     if gap % b == 0:
    #         return "Yes"
    #     else:
    #         if x_no == False:
    #             return "No"
    #         else:
    #             return "Yes"
            
    # else:
    #     return "Yes3"

    # gap in between
    gap = max(x2 - (x1+a), x1 - (x2 + a))

    if gap % a == 0:
        return "Yes"
    
    gap = max(y2 - (y1+b), y1 - (y2 + b))

    if gap % b == 0:
        return "Yes"
    else:
        return "No"
    
    
    

    



t = int(input())

for _ in range(t):
    print(solve())