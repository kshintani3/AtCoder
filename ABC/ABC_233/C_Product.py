import itertools

N, X = map(int, input().split())

li = [1]
for _ in range(N):
    _, *a = list(map(int, input().split()))
    li = [x * y for x, y in itertools.product(li, a) if X % (x * y) == 0]
print(li.count(X))
