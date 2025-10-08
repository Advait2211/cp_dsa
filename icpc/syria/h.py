def solve():
    n = int(input())
    a = list(map(int, input().split()))

    # max_moves = sum(a) - 1
    # min_moves = len(a) + a[-1] - 2

    # choice = max_moves - min_moves

    # return "First" if choice % 2 == 1 else "Second"

    """
    it does not make sense to consider more than the first 2 j's

    we will have a greedy choice between going to the next row, or going right


    """

    # cases 
    # want odd
    # want even
    # don w odd
    # don w even

    last = 1 if a[-1] % 2 == 0 else -1
    want = False if last == 1 else True

    for i in range(n-2, -1, -1):
        if want == False:
            if a[i] % 2 == 0:
                last = 1
            else:
                last = -1
        else:
            last = 1

        want = True if last == -1 else False

    if last == 1:
        return "First"
    else:
        return "Second"



        




t = int(input())
for _ in range(t):
    print(solve())