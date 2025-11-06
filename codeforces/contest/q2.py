def solve():
    n, q = map(int, input().split())
    s = input()
    a = list(map(int, input().split()))


    # s2= reversed(s)

    # itr = 1

    # for th in s2:
    #     if th == 'A':
    #         itr += 1
    #     else:
    #         itr *= 2

    # return itr


    # count = [0] * q

    temp = set(s)
    if len(temp) == 1 and 'A' in temp:
        for z in range(len(a)):
            print(a[z])
    else:
        for z in range(q):
            count = 0
            i = 0
            while a[z] > 0:
                count += 1
                if s[i] == 'A':
                    a[z] -= 1
                else:
                    a[z] = a[z] // 2
                
                if i == n-1:
                    i = 0
                else:
                    i += 1

            print(count)






    



t = int(input())
for _ in range(t):
    solve()