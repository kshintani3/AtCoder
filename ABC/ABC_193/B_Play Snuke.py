N = int(input())
can_b = []
for _ in range(N):
    A, P, X = map(int, input().split())
    if A < X:
        can_b.append(P)
if len(can_b) == 0:
    print(-1)
else:
    print(min(can_b))
