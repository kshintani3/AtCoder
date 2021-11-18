N, K = map(int, input().split())
p = list(map(int, input().split()))
e_li = [0]

for i in range(1, max(p) + 1):
    e_li.append((1 + i) * i / (2 * i))

ans = 0
for i in p[:K]:
    ans += e_li[i]

k_sum = ans
for i in range(N - K):
    k_sum = k_sum - e_li[p[i]] + e_li[p[i + K]]
    if k_sum > ans:
        ans = k_sum
print(ans)
