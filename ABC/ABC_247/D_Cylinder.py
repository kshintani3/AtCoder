from collections import deque

q = int(input())
qli = []
for _ in range(q):
    qli.append(list(map(int, input().split())))

tt = deque()
for i in qli:
    if i[0] == 1:
        tt.append([i[1], i[2]])
    if i[0] == 2:
        ans, cn = 0, i[1]
        while cn > 0:
            tt2 = tt.popleft()
            if tt2[1] >= cn:
                tt.appendleft((tt2[0], tt2[1] - cn))
                ans += tt2[0] * cn
                cn = 0
            else:
                ans += tt2[0] * tt2[1]
                cn = cn - tt2[1]
        print(ans)
