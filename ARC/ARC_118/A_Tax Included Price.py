import numpy as np

t, N = map(int, input().split())
P = 100 + t  # 周期

A = np.ones(P, np.bool_)
for x in range(100):
    A[P * x // 100] = 0

B = np.where(A)[0]  # P 以下で、税込み価格にならない金額
q, r = divmod(N - 1, t)  # 何回目の周期の、何番目か
ans = P * q + B[r]
print(ans)
