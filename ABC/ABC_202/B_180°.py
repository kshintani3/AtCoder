a = input().split()
alen = len(a)
ar = [0] * alen

for i in range(alen):
    ar[alen - i - 1] = a[i]

print(ar)

ans = "".join(ar)

print(ans.replace('6', 'X').replace('9', '6').replace('X', '9'))
