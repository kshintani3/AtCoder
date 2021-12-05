S, P = map(int, input().split())

ans = 0
for i in range(1, int(P ** 0.5) + 1):
    j = S - i
    if i * j == P:
        print("Yes")
        exit()
print("No")
