N, K = map(int, input().split())
p = list(map(int, input().split()))

e_li = [sum(p[0:K])]
for i in range(N - K):
    e_li.append(e_li[i] - p[i] + p[i + K])
print((max(e_li) + K) / 2)
# max(e_li) = pi + pi+1 + ... + pi+K-1
# ans = (1 + pi)/2 + (1 + pi+1)/2 + ... + (1 + pi+K-1)/2
