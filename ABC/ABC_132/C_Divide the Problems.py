N = int(input())
d = list(map(int, input().split()))
d_s = sorted(d)

print(d_s[N // 2] - d_s[N // 2 - 1])
