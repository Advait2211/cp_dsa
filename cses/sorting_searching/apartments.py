import sys
input = sys.stdin.readline

def solve():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a = sorted(a)
    b = sorted(b)

    """
    60 45 80 60
    30 60 75

    n - 45 60 60 80
    m - 30 60 75

    """
    m_explored = len(b) - 1
    soln = 0
    p = len(a) - 1
    q = len(b) - 1

    while p != -1 and q != -1:
        if a[p] - k <= b[q] <= a[p] + k:
            soln += 1
            p -= 1
            q -= 1
        elif a[p] - k > b[q]:
            p -= 1
        elif b[q] > a[p] + k:
            q -= 1

    # for i in range(len(a)-1, -1, -1):
    #     while m_explored != -1:
    #         if a[i] - k <= b[m_explored] <= a[i] + k:
    #             m_explored -= 1
    #             soln += 1
    #             break
    #         m_explored -= 1
    #         if a[i] + k > b[m_explored]:
    #             break

        # if m_explored == -1:
        #     break

    # print(a)
    # print(b)
        
    print(soln)
    
    

if __name__ == "__main__":
    solve()
