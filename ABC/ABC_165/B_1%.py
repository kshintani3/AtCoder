X = int(input())
bank = 100
ans = 0
while bank < X:
    bank += bank // 100
    ans += 1
print(ans)
