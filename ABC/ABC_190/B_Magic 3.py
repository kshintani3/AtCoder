import sys

N, S, D = map(int, input().split())
a = []
b = []

for _ in range(N):
    X, Y = map(int, input().split())
    if X < S and Y > D:
        print("Yes")
        sys.exit()
print("No")
