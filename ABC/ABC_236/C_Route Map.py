N, M = map(int, input().split())
s = list(input().split())
t = list(input().split())

ti = 0
for i in range(N):
    if s[i] == t[ti]:
        print("Yes")
        ti += 1
    else:
        print("No")
