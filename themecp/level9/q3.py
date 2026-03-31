# https://codeforces.com/contest/2070/problem/B
 
def solve():
    n, x, k = map(int, input().split())
    s = input()
    counter = 0
 
    left_count = 0
    right_count = 0
 
    if x == 0:
        for char in s:
            if char == "L":
                left_count += 1
            else:
                right_count += 1
 
            if left_count == right_count:
                return (k // (left_count + right_count)) + 1
 
        return 1
 
    left = 0
    right = 0
    direction = 0
 
    time_taken = 0
    total_time_taken = 0
    updated = False
    x2 = int(x)
 
    for val in s:
        if val == "L":
            x2 -= 1
            direction -= 1
            if left > direction:
                left = direction
        else:
            x2 += 1
            direction += 1
            if direction > right:
                right = direction
 
        time_taken += 1
 
        if x2 == 0 and not updated:
            total_time_taken = time_taken
            updated = True
            
 
        # print(left, right, direction)
 
    if x > 0:
        if x + left > 0:
            return 0
        else:
            for char in s:
                if char == "L":
                    left_count += 1
                else:
                    right_count += 1
 
                if left_count == right_count:
                    return ((k-total_time_taken) // (left_count + right_count)) + 1
 
            return 1
            
 
    if x < 0:
        if x + right < 0:
            return 0
        else:
            for char in s:
                if char == "L":
                    left_count += 1
                else:
                    right_count += 1
 
                if left_count == right_count:
                    return ((k-total_time_taken) // (left_count + right_count)) + 1
 
            return 1
    
 
 
t = int(input())
 
for _ in range(t):
    print(solve())