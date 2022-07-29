N, Q = map(int, input().split())
s = input()
top = 0

for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        top = (top - x) % N
    else:
        print(s[(top + x - 1) % N])
