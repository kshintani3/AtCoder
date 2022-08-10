a, b, c = map(int, input().split())
a %= 10
b %= 4
c %= 4
if b == 0: b = 4
if c == 0: c = 4
print((a ** (b ** c)) % 10)
