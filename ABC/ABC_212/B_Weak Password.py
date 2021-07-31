import collections

s = input()
a = [int(c) for c in s]

if len(collections.Counter(a)) == 1:
    print("Weak")
else:
    c = 0
    for i in range(3):
        if (int(a[i]) + 1) % 10 == a[i + 1]:
            c += 1
    if c == 3:
        print("Weak")
    else:
        print("Strong")
