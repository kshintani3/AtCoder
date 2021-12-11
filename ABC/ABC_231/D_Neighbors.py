N, M = map(int, input().split())
li = [[] for i in range(N + 1)]
if M == 0:
    print("Yes")
    exit()

for _ in range(M):
    a, b = map(int, input().split())
    li[a].append(b)
    li[b].append(a)
    if len(li[a]) > 2 or len(li[b]) > 2:
        print("No")
        exit()

locked = [False] * (N + 1)
one_li = []
for i in range(1, N + 1):
    if len(li[i]) == 1:
        one_li.append(i)
    elif len(li[i]) == 0:
        locked[i] = True

for one in one_li:
    if locked[one]:
        continue
    p = one
    nt = li[one][0]
    while True:
        locked[p] = True
        if len(li[nt]) == 1:
            locked[nt] = True
            break
        else:
            if li[nt][0] == p:
                nt, p = li[nt][1], nt
            else:
                nt, p = li[nt][0], nt
print("Yes" if sum(locked[1:]) == N else "No")
