H = int(input())
ans = 0
for i in range(40):
    ans += 2 ** i
    H = H // 2
    if H == 0:
        print(ans)
        exit()
