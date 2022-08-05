l1, r1, l2, r2 = map(int, input().split())
if l1 <= l2:
    if r1 <= r2:
        print(max(0, r1 - l2))
    else:
        print(r2 - l2)
else:
    if r2 <= r1:
        print(max(0, r2 - l1))
    else:
        print(r1 - l1)
