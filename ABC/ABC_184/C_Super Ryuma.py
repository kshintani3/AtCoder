R1, C1 = map(int, input().split())
R2, C2 = map(int, input().split())

R = R2 - R1
C = C2 - C1

if (R, C) == (0, 0):
    ans = 0
elif R == C or R == -C:
    ans = 1
elif abs(R) + abs(C) <= 3:
    ans = 1
elif abs(R) + abs(C) <= 6:
    ans = 2
elif (R ^ C ^ 1) & 1:
    ans = 2
elif abs(R + C) <= 3 or abs(R - C) <= 3:
    ans = 2
else:
    ans = 3

print(ans)
