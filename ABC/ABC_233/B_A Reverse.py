L, R = map(int, input().split())
s = input()
sr = s[L - 1:R]
print(s[:L - 1] + sr[::-1] + s[R:])
