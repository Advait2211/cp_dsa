import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    """
    what is the problem here? 
    count(2) = freq(2) + freq(3) + 2 * freq[4] + sum of other frequencies (gt4)
    count(3) = freq(3) + freq(4, 5) + 2 * freq[6] + sum of other frequencies (gt6)

 
    the minimum answer is the length of the array
    so the answer would be max(n, count(max(count)))


    how to find out the max_count? 
    store frequency of variables at index in an array ? 
    """

    reach = max(a) + 1

    freq = [0] * (reach)

    psum = [0] * (reach)

    for val in a:
        freq[val] += 1

    for i in range(1, reach):
        psum[i] = psum[i-1] + freq[i]

    # print(psum)

    mx = n

    for i in range(1, reach):
        temp = psum[-1] - psum[i-1]
        temp2 = freq[i * 2] if i * 2 <= reach-1 else 0
        mx = max(mx, temp+temp2)

    return mx

    
    


t = int(input())
for _ in range(t):
    print(solve()) 