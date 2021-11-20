N, X = map(int, input().split())
a = list(map(int, input().split()))
a_t = [False] * N
X -= 1
a_t[X] = True
for i in range(N):
    X = a[X] - 1
    a_t[X] = True
print(sum(a_t))
