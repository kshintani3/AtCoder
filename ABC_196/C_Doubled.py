n = int(input())
i = 0
count = 0
x = 1
flag = False

for s in range(1, 7):
    for t in range(i, (10 ** s)-1):
        i += 1
        x = (10 ** s) * i + i
        if x > n:
            flag = True
            break
        count += 1
    if flag:
        break

print(count)