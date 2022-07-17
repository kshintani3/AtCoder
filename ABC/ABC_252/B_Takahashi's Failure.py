N, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [False] * (N + 1)
for i in b: c[i] = True

am = max(a)
for j in range(N):
    if a[j] == am and c[j + 1]:
        print('Yes')
        exit()
print('No')
