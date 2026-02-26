def solve():
    n = int(input())
    a = input()

    if '1' not in a:
        print(0)
        return
    zeros = 0
    ones = 0
    lz = []
    oz = []

    for i in range(len(a)):
        val = a[i]
        if val == '0':
            zeros += 1
            lz.append(i+1)
        else:
            ones += 1
            oz.append(i+1)

    if zeros == 1:
        print(1)
        print(*lz)
        return

    if ones % 2 == 0:
        print(ones)
        print(*oz)
    elif zeros % 2 == 1 and ones % 2 == 1:
        print(zeros)
        print(*lz)
    else:
        print(-1)

    """
    100 - 111 - 100
    10101010 - 11010101 - 00010010 - 11111101 - 00000000 

    10101 - 00010 - 11111
    
    10 10 10 - 00 01 01 - 11 11 10 - 11 11 11

    00 00 11 - 01 11 00 - 11 00 11 - 00 01 00 - 11 11 11

    00 11 11 - 01 00 00 - 11 11 11

    00 00 11 - 11 11 10 - 00 00 00

    00 11 11 - 11 10 00 - 00 00 11 - 11 11 10 - 00 00 00


    00 01 - 01 10  - 11 01  - 00 00 

    001 - 010 - 111

    01

    1100000 - 10 11111 - 00 00000

    11 - 10 - 00

    """


t = int(input())
for _ in range(t):
    solve()
    # print()