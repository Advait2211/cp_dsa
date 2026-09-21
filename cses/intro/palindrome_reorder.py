def solve():
    s = input().strip()

    from collections import Counter
    freq = Counter(s)

    odd = False

    for key, value in freq.items():
        if odd and value % 2 == 1:
            print("NO SOLUTION")
            return
        
        if value % 2 == 1:
            odd = True

    start = ""
    end= ""
    mid = ""

    for key, value in freq.items():
        if value % 2 == 1:
            mid += value * key
        else:
            val = value // 2
            start += val * key
            end += val * key

    end = end[::-1]

    print(start + mid + end)




solve()