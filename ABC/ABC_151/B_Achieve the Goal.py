N, K, M = map(int, input().split())
a = list(map(int, input().split()))
ans = N * M - sum(a)
print(max(ans, 0) if ans <= K else -1)
