n = int(input())
c = list(map(int, input().split()))

c.sort()
ans = c[0]

count = 0
flag = False

for i in range(1, n):
    if count == c[i] + 1:
        count += 1
    elif count == c[i]:
        flag = True
        break
    ans *= c[i] - i
    ans %= 10 ** 9 + 7

if flag:
    print(0)
else:
    print(ans)
