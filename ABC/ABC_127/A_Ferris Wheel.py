A, B = map(int, input().split())
ans = B // 2 if A < 13 else B
print(ans if A >= 6 else 0)
