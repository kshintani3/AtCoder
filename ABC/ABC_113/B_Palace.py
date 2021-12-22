N = int(input())
T, A = map(int, input().split())
h = list(map(int, input().split()))

ans = 0
mi = float('inf')
for i, v in enumerate(h):
    if mi > abs(T - 0.006 * v - A):
        mi = abs(T - 0.006 * v - A)
        ans = i
print(ans + 1)
