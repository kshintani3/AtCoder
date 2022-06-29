xl = []
yl = []
for _ in range(3):
    x, y = map(str, input().split())
    xl.append(x)
    yl.append(y)

xl.sort()
yl.sort()

if xl[0] == xl[1]:
    print(xl[2], end=" ")
else:
    print(xl[0], end=" ")

if yl[0] == yl[1]:
    print(yl[2], end=" ")
else:
    print(yl[0], end=" ")
