def dis(xa, ya, xb, yb):
    return (xa - xb) ** 2 + (ya - yb) ** 2


x1, y1, x2, y2 = map(int, input().split())

for xs in range(-2, 3):
    for ys in range(-2, 3):
        x = x1 - xs
        y = y1 - ys
        if dis(x, y, x1, y1) == 5 and dis(x, y, x2, y2) == 5:
            print("Yes")
            exit()
print("No")
