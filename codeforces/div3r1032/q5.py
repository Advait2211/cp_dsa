def count_common_prefix(a, b):
    str_a, str_b = str(a), str(b)
    count = 0
    for digit_a, digit_b in zip(str_a, str_b):
        if digit_a == digit_b:
            count += 1
        else:
            break
    return count

def solve():
    t = int(input())
    for _ in range(t):
        l, r = input().split()
        count = 0
        for a, b in zip(l, r):
            if a == b:
                count += 1
            else:
                break
        print(2 * count)

solve()
