import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    from collections import defaultdict, Counter

    """
    1 1 1 1 2 2 2 2 2 2 2 2

    1 2 2 2 2 2  1 1 1 2 2 2

    1 1 1 1 2 2 2 2 3 3 3 3 4 4 4 4

    _ _ _ _ _ _ _ _      _ _ _ _ _ _ _ _ 
    1 2 3 3 3 4 4 4      1 1 1 2 2 2 3 4

    


    1 1 1 1 2 3 4 5

    1 2 3 4  1 1 1 5
    """

    # freq = defaultdict(int)

    # vals = set()
    # blacklist = set()

    # cnt = 0

    # for val in a:
    #     if val in blacklist:
    #         continue
    #     if val % 2 == 0:
    #         continue
    #     if val in vals:
    #         blacklist.add(val)
    #         cnt += 1
    #     else:
    #         vals.add(val)
    #         cnt += 1

    # return cnt

    freq = Counter(a)
    soln = 0
    offsets = True

    odd = False

    # print(freq)

    for key, value in freq.items():
        # print(value)
        if value % 2 == 0:
            if value % 4 == 0:
                # print("in")
                offsets = not offsets
                # print(offsets)
                if offsets:
                    soln += 4
            else:
                soln += 2
        else:
            odd = True
            soln += 1

    if not offsets and odd:
        soln += 2

    # print(offsets)

    return soln

        

    


t = int(input())
for _ in range(t):
    print(solve()) 