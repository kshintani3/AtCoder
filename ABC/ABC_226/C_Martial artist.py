from collections import deque

N = int(input())
T = [0]
K = [0]
a_list = [[]]
get = [False] * (N + 1)

for _ in range(N):
    inp = list(map(int, input().split()))
    T.append(inp[0])
    K.append(inp[1])
    if K != 0:
        a_list.append(inp[2:])
    else:
        a_list.append([])

if K[-1] == 0:
    print(T[-1])
else:
    q = deque([N])
    while len(q) != 0:
        a = q.pop()
        if get[a]:
            continue
        get[a] = True
        if K[a] != 0:
            for i in a_list[a]:
                q.append(i)

    ans = 0

    for i in range(1, N + 1):
        if get[i]:
            ans += T[i]
    print(ans)
