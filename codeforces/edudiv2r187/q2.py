def solve():
    n = input()
 
    a = []
 
    for val in n:
        a.append(int(val))
 
    suma = sum(a)
    if suma < 10:
        return 0
    
    a = [a[0]] + sorted(a[1:], reverse=True)
 
    # print(a)
 
    if a[0] == 1:
        oth = 0
        for i in range(1, len(a)):
            oth += a[i]
            if (suma - oth) < 10:
                return i
 
    else:
        og = a[0] - 1
        oth = 0

        if (suma - og) < 10:
            return 1
 
        # a = sorted(a, reverse=True)
        for i in range(1, len(a)):
            og += a[i]
            oth += a[i]
 
            if (suma - oth) < 10:
                return i 
            if (suma - og) < 10:
                return i+1
        
    
 
 
 
 
t = int(input())
for _ in range(t):
    print(solve())