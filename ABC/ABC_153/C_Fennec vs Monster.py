H, K = map(int, input().split())
a = sorted(list(map(int, input().split())), reverse=True)
print(sum(a[K:]))
