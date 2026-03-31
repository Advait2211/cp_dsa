# https://codeforces.com/contest/1760/problem/C

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    
    maxi = max(a)
    largest = -1
    second_largest = -1
    
    for num in a:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
        
    # print(largest, second_largest)
    
    soln = []
    
    for num in a:
        if num == largest:
            soln.append(largest - second_largest)
        else:
            soln.append(num - largest)
            
    print(*soln)
 
 
t = int(input())
 
for _ in range(t):
    solve()