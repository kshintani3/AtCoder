def kaibun():
    s = input()
    a = [int(c) for c in s]
    b = len(a)
    c = 0
    ans = "Yes"
    kosuu = 0
    for i in range(b):
        if a[ b - i - 1 ] != 0:
            kosuu = b-i
            break
    if kosuu % 2 == 0:
        c = int(kosuu / 2)
    else:
        c = int((kosuu-1) / 2)
    for s in range(c):
        if a[s] != a[kosuu - 1 - s]:
            ans = "No" 
            break
    print(ans)
kaibun()