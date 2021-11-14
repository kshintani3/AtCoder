N, K = map(int, input().split())
a = list(map(int, input().split()))
a = sorted(a, reverse=True)
N_K = N // K
ans = 0
if K == 1:
    print(sum(a))
    exit()
for i in reversed(range(1, N_K + 1)):
    KK = i * K
    while True:
        a_left = a[KK - 1]
        if a_left == 0:
            break
        ans += a_left * i
        for j in range(KK):
            a[j] -= a_left
        a = sorted(a, reverse=True)
print(ans)
