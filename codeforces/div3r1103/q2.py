import sys
input = sys.stdin.readline

from collections import Counter

def solve():
    n = int(input())
    a = input().strip()

    if n == 1:
        return 0

    if n == 2:
        if len(set(a)) == 1:
            return 1
        else:
            return 0

    if len(set(a)) == 1:
        return -1


    '''
    potential failure scenarios:
    all are the same and len >= 3

    otherwise if the count of one element is greater than the other + 2, then after equal deletion it is not possible to have this

    once we determine it is possible to do, we need to find all the islands and then just dissolve them

    '''


    freq = Counter(a)

    if freq['0'] > freq['1'] + 2:
        return -1

    if freq['1'] > freq['0'] + 2:
            return -1


    '''
    now the idea is simple
    whatever happens, the question is now solvable. 
    so disolving is the island is just deleting all values but the first and last (from the sequence)
    except for the first and last series'
    '''

    dele = 0

    dl = []

    l, r = 0, 1



    # while r < n:
        # while r < (n-1) and a[r] == a[l]:
        #     r += 1

        # if a[l] == 0 or a[r] == n-1:
        #     dele += (r - l) - 1
        # else:
        #     dele += (r - l) - 2

        # l = r

        # r += 1

    while r < n:
        if a[l] == a[r]:
            dl.append(a[r])
            dele += 1
            r += 1
        else:
            l = r
            r += 1

    diff = max(dl.count('1'), dl.count('0')) - min(dl.count('1'), dl.count('0'))

    diff = max(diff-1, 0)
    return(dele + diff)

    
    


t = int(input())
for _ in range(t):
    print(solve()) 