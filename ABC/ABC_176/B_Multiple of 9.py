N = input()
ans = 0
for i in N:
    ans += int(i)
print("Yes" if ans % 9 == 0 else "No")
