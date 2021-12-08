m = 0
t = 0
for _ in range(5):
    a = int(input())
    t += a
    if a % 10 > 0:
        t += 10 - a % 10
        m = max(10 - a % 10, m)
print(t - m)
