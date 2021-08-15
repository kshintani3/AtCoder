s, t = map(int, input().split())
s += 1
ans = 0

for i in range(s):
    for j in range(s - i):
        for n in range(s - i - j):
            if (i * j * n <= t):
                ans += 1
print(ans)
