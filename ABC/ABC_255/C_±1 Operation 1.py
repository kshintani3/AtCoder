X, A, D, N = map(int, input().split())
if D < 0:
    A = D * (N - 1) + A
    D *= -1

dn = D * (N - 1) + A
if X <= A:
    print(A - X)
elif X >= dn:
    print(X - dn)
else:
    x_d = (X - A) % D
    print(min(x_d, D - x_d))
