a, b, c = map(int, input().split())
print("Yes" if sorted([a, b, c])[1] == b else "No")
