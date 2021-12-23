s = input()
N = int(input())
x, y = "", ""
flag = False
for _ in range(N):
    q = input()
    if q[0] == "1":
        flag = not flag
    else:
        if (flag + int(q[2])) % 2 == 1:
            x = q[4] + x
        else:
            y += q[4]
s = x + s + y
print(s if not flag else s[::-1])
