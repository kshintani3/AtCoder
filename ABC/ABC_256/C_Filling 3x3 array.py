h1, h2, h3, w1, w2, w3 = map(int, input().split())

ans = 0

for a in range(1, min(h1, w1) - 1):
    for b in range(1, min(h1, w2) - 1):
        for c in range(1, min(h2, w1) - 1):
            for d in range(1, min(h2, w2) - 1):
                ac = a + c
                ab = a + b
                bd = b + d
                cd = c + d
                if h1 > ab and w1 > ac and h2 > cd and w2 > bd:
                    h = w1 - ac + w2 - bd
                    w = h1 - ab + h2 - cd
                    if h3 - h == w3 - w and w3 > w:
                        ans += 1
print(ans)
