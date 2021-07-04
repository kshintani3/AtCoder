a, b = map(int, input().split())

ans = ((a * (a + 1) // 2) * b) * 100 + ((b * (b + 1) // 2) * a)
print(ans)
