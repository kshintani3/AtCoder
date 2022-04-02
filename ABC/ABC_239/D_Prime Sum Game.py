A, B, C, D = map(int, input().split())

so = []
for i in range(2, 200):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        so.append(i)

for x in range(A, B + 1):
    flag = True
    for y in range(C, D + 1):
        if x + y in so:
            flag = False
            break
    if flag:
        print("Takahashi")
        exit()
print("Aoki")
