N, M = map(int, input().split())
if M <= N:
    print(0)
    exit()

x = list(map(int, input().split()))
x.sort()
y = []
for i in range(M - 1):
    y.append(x[i + 1] - x[i])

ans = sum(y)
y.sort()
for j in range(1, N):
    ans -= y[-j]
print(ans)
