N, K, Q = map(int, input().split())
N_point = [K] * N
A_list = [0] * N
for _ in range(Q):
    A_list[int(input()) - 1] += 1
for n, a in zip(N_point, A_list):
    print("Yes" if n + a - Q > 0 else "No")
