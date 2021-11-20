N = int(input())
a = []
a_ma = 0
a_ma_2 = 0
for _ in range(N):
    A = int(input())
    a.append(A)
    if a_ma <= A:
        a_ma_2 = a_ma
        a_ma = A
    else:
        a_ma_2 = max(A, a_ma_2)
for i in a:
    print(a_ma_2 if i == a_ma else a_ma)
