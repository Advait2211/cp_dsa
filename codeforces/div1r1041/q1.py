

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    a = set(arr)

    if 0 in a:
        return "No"
    else:
        if -1 in a:
            if len(a) <= 2:
                return "Yes"
            else:
                return "No"
            
        if len(a) > 1:
            return "No"

        return "Yes"
    
    
 
 
t = int(input())
 
for _ in range(t):
    print(solve())