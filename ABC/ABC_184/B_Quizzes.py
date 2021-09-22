_, X = map(int, input().split())
s = list(input())

for i in s:
    if i == "o":
        X += 1
    else:
        X -= 1
        if X < 0:
            X = 0
print(X)
