N, K = map(int, input().split())
N_list = [True] * N
ck_list = [0] * N

for i in range(1, K + 1):
    c, k = input().split()
    k = int(k)
    if c == "L":
        for j in range(k, N):
            ck_list[j] += 1
    else:
        for j in range(0, k):
            ck_list[j] += 1
    N_list[k - 1] = False
ans = 1
for i in range(N):
    if N_list[i]:
        ans *= ck_list[i]
print(ans % 998244353)
