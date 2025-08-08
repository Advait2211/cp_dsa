

def solve():
    n, x = map(int, input().split())
    a = input()

    l = r = lp = rp = 0
    last_l, first_r = -1, -1

    for i, val in enumerate(a, start=1):
        if i < x:
            if val == '#':
                l += 1
                last_l = i
            else:
                lp += 1
        elif i > x:
            if val == '#':
                if r == 0:
                    first_r = i
                r += 1
            else:
                rp += 1
        # print(r)

    # print(r, l)

    l_possible = x - l - 1
    r_possible = n - x - r

    # print(l_possible, l)

    if (r_possible == 0 and r == 0) or (l_possible == 0 and l == 0):
        return 1
    elif r == 0 and l == 0:
        return 1
    else:
        # print(r, r_possible)
        # print(l, l_possible)

        print(n - first_r, last_l, l+lp, r+rp)
        # if (n - first_r) > last_l:
        #     return min(r+rp+1, last_l)
        # else:
        #     return min(l+lp+1, first_r)

        if (n - first_r) > last_l:
            return min(n - first_r, l+lp) + 1
        elif last_l > (n - first_r):
            return min(last_l, r+rp) + 1
        else:
            return min(r+rp, l+lp) + 1
        
        return min(max(n - first_r, last_l), l+lp, r+rp) + 1
    
        
    
    # []

    # 4 4 3 3 
    # 3 4
    # 3 4

    
    
 
 
t = int(input())
 
for _ in range(t):
    # print("output: ")
    print(solve())