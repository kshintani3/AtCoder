N = int(input())
cn = 0

for _ in range(N):
    d1, d2 = map(int, input().split())
    if d1 == d2:
        cn += 1
    else:
        cn = 0
    if cn >= 3:
        print("Yes")
        exit()
print("No")
