s = input()
sl = len(s)
rl, lr = [], [0]
ans = [0] * sl

for i in range(sl - 1):
    if s[i:i + 2] == 'RL':
        rl.append(i)
    if s[i:i + 2] == 'LR':
        lr.append(i + 1)
lr.append(sl)

for i in range(len(rl)):
    a = rl[i]
    l, r = lr[i], lr[i + 1] - 1
    ans[a] = 1 + (a - l) // 2 + (r - a) // 2
    ans[a + 1] = 1 + (a + 1 - l) // 2 + (r - a - 1) // 2
print(*ans)
