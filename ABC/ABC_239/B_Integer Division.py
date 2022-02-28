X = int(input())

for i in range(10):
    if X % 10 == 0:
        break
    else:
        X -= 1
print(X // 10)
