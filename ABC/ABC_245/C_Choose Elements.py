N, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

q = [a[0], b[0]]
for i in range(1, N):
    ab = []
    for qi in q:
        if abs(qi - a[i]) <= K:
            ab.append(a[i])
        if abs(qi - b[i]) <= K:
            ab.append(b[i])

    if len(ab) < 1:
        print('No')
        exit()
    q = set(ab)
print('Yes')
