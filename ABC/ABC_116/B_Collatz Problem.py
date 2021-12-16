s = int(input())
li = [False] * 1000000
ans = 1
while True:
    li[s] = True
    if s % 2 == 0:
        s = int(s // 2)
    else:
        s = 3 * s + 1
    ans += 1
    if li[s]:
        print(ans)
        exit()
