N = int(input())
st = [input().split() for _ in range(N)]

for i in range(N - 1):
    for j in range(i + 1, N):
        if st[i] == st[j]:
            print("No")
            exit()

for i in range(N):
    sfl = False
    tfl = False
    si, ti = st[i]
    for j in range(N):
        if i == j:
            continue
        if si in st[j]:
            sfl = True
        if ti in st[j]:
            tfl = True
    if sfl and tfl:
        print("No")
        exit()
print("Yes")
