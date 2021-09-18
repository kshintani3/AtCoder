import sys

N, X = map(int, input().split())
X *= 100

for ans in range(N):
    V, P = map(int, input().split())
    X -= V * P
    ans += 1
    if 0 > X:
        print(ans)
        sys.exit()
print(-1)
