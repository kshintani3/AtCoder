K, N = map(int, input().split())
a = list(map(int, input().split()))
a_d = [a[i] - a[i - 1] for i in range(N)]
a_d[0] += K

print(sum(a_d) - max(a_d))
