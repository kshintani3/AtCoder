_, _, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

print("No War" if max(x) < min(y) and max(x) < Y and X < min(y) else "War")
