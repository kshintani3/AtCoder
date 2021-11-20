N, K = map(int, input().split())
p_4 = []
for _ in range(N):
    p = list(map(int, input().split()))
    p_4.append(sum(p))
p_s = sorted(p_4)
s_ma = p_s[-K]

for i in p_4:
    if i + 300 - s_ma >= 0:
        print("Yes")
    else:
        print("No")
