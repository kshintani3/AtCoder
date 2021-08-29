X, Y = input().split(".")
Y = int(Y)

if Y < 3:
    print(X + "-")
elif Y < 7:
    print(X)
else:
    print(X + "+")
