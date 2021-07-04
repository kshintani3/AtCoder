a, b = map(int, input().split())
ans = float(a * b / 100)
if a * b % 100 == 0:
    print(int(ans))
else:
    print(ans)
