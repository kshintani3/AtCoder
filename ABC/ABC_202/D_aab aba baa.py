def kai(x, y, z):
    import math
    total = math.factorial(x + y) // (math.factorial(x) * math.factorial(y))
    out = (total * x) // (x + y)
    if out >= z:
        ab = 'a'
    else:
        ab = 'b'
        z = z - out
    # print(k)
    return ab, z


a, b, k = map(int, input().split())
ans = []

for i in range(a + b):
    ab, k = kai(a, b, k)
    if ab == 'a':
        a -= 1
    else:
        b -= 1
    ans.append(ab)
print(''.join(map(str, ans)))
