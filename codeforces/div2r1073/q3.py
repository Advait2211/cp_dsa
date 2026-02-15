def solve():
    n = int(input())
    a = input()

    # if len(set(a)) == 1:
    #     print("Bob")
    #     return

    count = 0

    # for i in range(0, n-1):
    #     if a[i+1] == '0' and a[i] == '1':
    #         count += 1

    # if count == 0:
    #     print("Bob")
    #     return
    
    # import math
    # ans = math.ceil(math.log2(count))

    # print(count)
    # print(ans)
    
    # soln = []

    # idx = a.find('1')
    # soln.append(idx+1)

    # # seen_zero = False

    # for i in range(idx, n):
    #     if a[i] == '1':
    #         pass
    #     else:
    #         soln.append(i + 1)

    # print("Alice")
    # print(len(soln))
    # print(*soln)

    ones = []
    zeros_prefix = []

    nim = 0
    zeros = 0

    for i in range(len(a) - 1, -1, -1):
        ch = a[i]
        if ch == '0':
            zeros += 1
            zeros_prefix.append(zeros)
        else:
            nim ^= zeros
            zeros_prefix.append(zeros)
            ones.append(i)


    if nim == 0:
        print("Bob")
        return
    
    print("Alice")

    mc_one = -1
    need = 0

    for pos in ones:
        goal = zeros_prefix[len(a) - 1 - pos] 
        target = goal ^ nim

        if target < goal:
            mc_one = pos
            need = goal - target
            break

    indices = [mc_one + 1]
    cnt = 0

    for j in range(mc_one + 1, len(a)):
        if a[j] == '0':
            indices.append(j + 1)
            cnt += 1
            if cnt == need:
                break

    print(len(indices))
    print(*indices)


t = int(input())
for _ in range(t):
    solve()