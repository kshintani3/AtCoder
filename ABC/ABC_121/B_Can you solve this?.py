N, M, C = map(int, input().split())
b = list(map(int, input().split()))
ans = 0
for _ in range(N):
    a = list(map(int, input().split()))
    ab = [ai * bi for ai, bi in zip(a, b)]
    if sum(ab) + C > 0:
        ans += 1
print(ans)
