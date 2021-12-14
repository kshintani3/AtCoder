N, M, X = map(int, input().split())
ca_li = []
ans = 10 ** 8
flag = False
for _ in range(N):
    ca_li.append(list(map(int, input().split())))
for i in range(2 ** N):
    tol = [-X] * M
    cn = 0
    s = (bin(i)[2:]).zfill(N)
    for j in range(N):
        if s[j] == "1":
            tol = [min(0, tol[a] + ca_li[j][a + 1]) for a in range(M)]
            cn += ca_li[j][0]
    if not any(tol):
        ans = min(cn, ans)
        flag = True
        # print(s, cn, tol)
print(ans if flag else -1)
