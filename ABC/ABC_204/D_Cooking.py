n = int(input())
a = list(map(int, input().split()))
oven1 = 0
oven2 = 0
count = 0

if n == 1:
    print(a[0])
else:
    a.sort()
    a.insert(0, 0)
    a.insert(0, 0)
    oven1 = a.pop(-1)
    oven2 = a.pop(-1)
    for i in range(n - 2):
        count = 0
        for j in range(2, n - i - 1):
            count += a[j]
            # print(count)
        if a[n - i - 1] >= count:
            if oven1 < oven2:
                oven1 += a[n - i - 1]
            else:
                oven2 += a[n - i - 1]
        else:
            if oven1 < oven2:
                oven2 += a[n - i - 1]
            else:
                oven1 += a[n - i - 1]
        # print(oven1,oven2)

    if oven1 > oven2:
        print(oven1)
    else:
        print(oven2)
