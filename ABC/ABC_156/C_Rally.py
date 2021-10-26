N = int(input())
a = list(map(int, input().split()))
ans = 1000000
for i in range(101):
    b = [(c - i) ** 2 for c in a]
    if ans > sum(b):
        ans = sum(b)
print(ans)
