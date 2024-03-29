import bisect

N = int(input())
l = list(map(int, input().split()))
l.sort()
ans = 0

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        ans += bisect.bisect_left(l, l[i] + l[j]) - j - 1
print(ans)
