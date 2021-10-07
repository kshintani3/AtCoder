X, K, D = map(int, input().split())
X = abs(X)
k_d = X // D

if k_d >= K:
    print(X - K * D)
else:
    K = (K - k_d) % 2
    X -= (k_d + K) * D
    print(abs(X))
