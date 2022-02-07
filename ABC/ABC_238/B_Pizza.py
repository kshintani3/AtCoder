N = int(input())
a = list(map(int, input().split()))
a_sum = 0
cut = [0]

for i in a:
    a_sum = (a_sum + i) % 360
    cut.append(a_sum)
if cut[-1] < 360:
    cut.append(360)

cut.sort()
ans = 0
for i in range(len(cut) - 1):
    ans = max(ans, cut[i + 1] - cut[i])
print(ans)
