n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

c = b[0] - a[-1] + 1
if c < 0:
    c = 0

print(c)
