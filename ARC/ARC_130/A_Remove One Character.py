N = int(input())
s = input()
s += "A"
pre_s = "A"
x, ans = 1, 0
for i in s:
    if pre_s == i:
        x += 1
    else:
        ans += x * (x - 1) // 2
        x = 1
    pre_s = i
print(ans)
