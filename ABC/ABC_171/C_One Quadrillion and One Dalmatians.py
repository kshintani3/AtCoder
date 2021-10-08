N = int(input()) - 1
ans = ""
for i in range(1, 12):
    ans += chr(N % 26 + 97)
    N = N // 26 - 1
    if N < 0:
        print(ans[::-1])
        exit()
