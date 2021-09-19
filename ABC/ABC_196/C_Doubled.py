import sys

N = int(input())
ans = 0

for s in range(1, 10 ** 7):
    x = s * 10 ** len(str(s)) + s
    if x > N:
        print(ans)
        sys.exit()
    ans += 1
