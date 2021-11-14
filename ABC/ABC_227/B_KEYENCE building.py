s_list = []
for a in range(1, 200):
    for b in range(1, 200):
        s_list.append(4 * a * b + 3 * a + 3 * b)
s_list = set(s_list)
_ = int(input())
s = list(map(int, input().split()))
ans = 0
for ss in s:
    if ss not in s_list:
        ans += 1
print(ans)
