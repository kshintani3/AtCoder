N = int(input())
ans = N

for i in range(1, N + 1):
    if "7" in str(i) or "7" in oct(i):
        ans -= 1

print(ans)
