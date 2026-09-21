import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    """
    have to check parity of the question

    so basically when you change a right side element, all the sign of the left side change

    so you have to ensure that when you are making the current element negative, all elements to the left are negative
    f it
    let us do dry runs to find that out

    assumption: value we do not consider at the current point in time
    we assume that most could be made positive is done effectively

    so essentially we have to find the point of maximum gain
    we should make all the elements before it negative - this is possible - we know how

    and then make the gain point negative.

    so what is the gain point?
    it is a value where making the values before it positive while making it negative

    so each index will have a gain value
    this is just the sum of negative values before it - its value

    the node which has the highest gain point is the optimal solution
    """


    neg = 0
    gain_arr = []

    for i in range(n):
        if a[i] < 0:
            gain_arr.append(-1)
            neg += -a[i]
        else:
            gain_arr.append(neg - a[i])

    # print(gain_arr)
    index = gain_arr.index(max(gain_arr))

    if max(gain_arr) < 0:
        print(0)
        print()
        return

    # if index == 0 or index == 1:
    #     print(0)
    #     print()
    #     return


    # making all before the gain point negative
    opr = 0
    idx = []

    for i in range(index-1, -1, -1):
        if (a[i] > 0 and opr % 2 == 0) or (a[i] < 0 and opr % 2 == 1):
            idx.append(i+1)
            opr += 1

    idx.append(index+1)
    print(len(idx))
    print(*idx)




    


t = int(input())
for _ in range(t):
    solve()