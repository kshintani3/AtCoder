H, W = map(int, input().split())
R, C = map(int, input().split())

if H + W == 2:
    print(0)
elif 1 in [H, W]:
    print(2 - (H + W == R + C))
else:
    print(4 - (R in [1, H]) - (C in [1, W]))
