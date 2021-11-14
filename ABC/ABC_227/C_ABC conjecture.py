N = int(input())
ans = 0
for a in range(1, int(N ** (1/3)) + 3):
    for b in range(a, N // a + 2):
        c = (N // (a * b))
        if c >= b:
            ans += c - b + 1
        else:
            break
print(ans)
