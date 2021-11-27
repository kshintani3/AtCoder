S = input()
K = int(input())
dots = [0]
d_cn = 0
for si in S:
    if si == ".":
        d_cn += 1
    dots.append(d_cn)

right = 0
left = 0
ans = 0

while right <= len(S):
    if dots[right] - dots[left] <= K:
        ans = max(ans, right - left)
        right += 1
    else:
        left += 1
print(ans)
