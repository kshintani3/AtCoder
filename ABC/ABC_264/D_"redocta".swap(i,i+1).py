s = [i for i in input()]
atc = 'atcoder'
ans = 0
for i in atc[:-1]:
    ans += s.index(i)
    s.remove(i)
print(ans)
