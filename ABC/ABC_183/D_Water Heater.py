import itertools

N, W = map(int, input().split())

w_list = [0] * (2 * 10 ** 5 + 1)
for _ in range(N):
    s, t, p = map(int, input().split())
    w_list[s] += p
    w_list[t] -= p

w_list = list(itertools.accumulate(w_list))

if max(w_list) <= W:
    print("Yes")
else:
    print("No")
