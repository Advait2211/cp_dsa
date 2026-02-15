import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    v = list(map(int, input().split()))

    mp = {}
    for i in range(n):
        mp[v[i]] = i

    st = []
    prev = [0] * n
    fc = set()

    for i in range(n):
        if v[i] not in fc:
            fc.add(v[i])

            if not st:
                st.append((mp[v[i]], i))
            else:
                tp_idx, tp_start = st[-1]
                if tp_idx > mp[v[i]]:
                    st.append((mp[v[i]], i))
                else:
                    st.pop()
                    st.append((mp[v[i]], tp_start))

        tp_idx, tp_start = st[-1]

        if i == tp_idx:
            if tp_start == 0:
                prev[i] = 1
            else:
                prev[i] = prev[tp_start - 1] + 1
            st.pop()

    print(sum(prev))
