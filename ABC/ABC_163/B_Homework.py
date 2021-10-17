N, _ = map(int, input().split())
a = list(map(int, input().split()))

print(-1 if N < sum(a) else N - sum(a))
