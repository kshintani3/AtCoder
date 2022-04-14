N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans_1 = 0

for i in range(N):
    if a[i] == b[i]:
        ans_1 += 1
print(ans_1)

ans = 0
a_set = set(a)
b_set = set(b)
for i in a_set:
    if i in b_set:
        ans += 1
print(ans - ans_1)
