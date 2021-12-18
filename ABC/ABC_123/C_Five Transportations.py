N = int(input())
ans = 0
for _ in range(5):
    ans = max(ans, (N - 1) // int(input()))
print(ans + 5)
