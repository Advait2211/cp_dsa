# https://codeforces.com/problemset/problem/2060/C

"""
logic:

"""


def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    need_dict = {}
    soln = 0

    for i in range(n):
        # check if current this is required by anything - so this is stupid. 
        # if not just add it to the dict

        # we have to add need to the dict, not the current val. then it is fixed. 

        if a[i] in need_dict:
            if need_dict[a[i]] == 1:
                del need_dict[a[i]]
            else:
                need_dict[a[i]] -= 1

            soln += 1
        
        else:
            # raise an requirement. 
            need = k - a[i]

            if need in need_dict:
                need_dict[need] += 1
            else:
                need_dict[need] = 1

    
    return soln



        
            
            
        


t = int(input())

for _ in range(t):
    print(solve())
