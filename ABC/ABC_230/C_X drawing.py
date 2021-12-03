N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

ans_li = [["."] * (S - R + 1) for _ in range(Q - P + 1)]
for i in range(Q - P + 1):
    for j in range(S - R + 1):
        if (i + P) - A == (j + R) - B:
            ans_li[i][j] = "#"
        if (i + P) - A == B - (j + R):
            ans_li[i][j] = "#"

for ans in ans_li:
    print("".join(ans))
