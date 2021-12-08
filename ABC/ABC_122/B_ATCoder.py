li = "ACTG"
S = input() + "B"
ans, cn = 0, 0
for si in S:
    if si in li:
        cn += 1
    else:
        if cn > ans:
            ans = cn
        cn = 0
print(ans)
