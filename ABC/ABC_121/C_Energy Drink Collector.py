N, M = map(int, input().split())
ab = []
for _ in range(N):
    ai, bi = map(int, input().split())
    ab.append((ai, bi))
ab = sorted(ab, key=lambda x: x[0])
total = 0
for a, b in ab:
    if M <= b:
        total += a * M
        print(total)
        exit()
    total += a * b
    M -= b
