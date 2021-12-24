N, T = map(int, input().split())
ans = 1001
for _ in range(N):
    Ci, Ti = map(int, input().split())
    if T >= Ti:
        ans = min(ans, Ci)
print(ans if ans < 1001 else "TLE")
