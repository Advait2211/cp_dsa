from collections import Counter

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    if n < 8:
        return 0
    
    for i in range(8, n + 1):
        freq_dict = Counter(a[:i])
        
        if (freq_dict.get(0, 0) >= 3 and freq_dict.get(1, 0) >= 1 and 
            freq_dict.get(2, 0) >= 2 and freq_dict.get(3, 0) >= 1 and 
            freq_dict.get(5, 0) >= 1):
            return i
    
    return 0

t = int(input())

for _ in range(t):
    print(solve())
