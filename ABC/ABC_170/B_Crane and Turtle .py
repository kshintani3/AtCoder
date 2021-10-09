X, Y = map(int, input().split())

if Y % 2 == 0 and Y / 4 <= X <= Y / 2:
    print("Yes")
else:
    print("No")
