A, B = map(int, input().split())

ans = 4 - ((A + B) >= 15 and B >= 8) - ((A + B) >= 10 and B >= 3) - ((A + B) >= 3)

print(ans)
