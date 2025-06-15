def solve():
    k, a, b, x, y = map(int, input().split())

    cooked = 0
    current_k = k

    if x <= y:

        if current_k >= a:
            num_type1 = (current_k - a) // x + 1
            cooked += num_type1
            current_k -= num_type1 * x

        if current_k >= b:
            num_type2 = (current_k - b) // y + 1
            cooked += num_type2

    else:
        
        if current_k >= b:
            num_type2 = (current_k - b) // y + 1
            cooked += num_type2
            current_k -= num_type2 * y

        if current_k >= a:
            num_type1 = (current_k - a) // x + 1
            cooked += num_type1
            
    return cooked

t = int(input())
for _ in range(t):
    print(solve())
