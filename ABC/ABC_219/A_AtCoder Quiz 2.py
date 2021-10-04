X = int(input())
score = [40, 70, 90]

for i in score:
    if i - X > 0:
        print(i - X)
        exit()
print("expert")
