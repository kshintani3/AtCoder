import collections

S = input()
s_cn = collections.Counter(S)

if len(S) <= 2:
    if int(S) % 8 == 0 or int(S[::-1]) % 8 == 0:
        print("Yes")
        exit()
else:
    for i in range(104, 1000, 8):
        x8_cn = collections.Counter(str(i))
        if not x8_cn - s_cn:
            print("Yes")
            exit()
print("No")
