s = input()
a = [int(c) for c in s]

a_list = []

if len(a) % 3 == 1:
    a.insert(0, 0)
    a.insert(0, 0)
elif len(a) % 3 == 2:
    a.insert(0, 0)

for i in range(len(a) // 3):
    b = a[3 * i] * 100 + a[3 * i + 1] * 10 + a[3 * i + 2]
    a_list.append(b)

b = int(s) - 10 ** ((len(a_list) - 1) * 3) + 1
ans = b * (len(a_list) - 1)

for i in range(1, len(a_list)):
    b = 10 ** ((len(a_list) - i) * 3) - 10 ** ((len(a_list) - i - 1) * 3)
    ans += b * (len(a_list) - i - 1)

print(ans)
