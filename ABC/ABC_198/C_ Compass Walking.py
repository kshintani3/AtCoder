import math
def hosuu():
    r, xg, yg = map(int,input().split())
    ans = 0
    kyori = math.sqrt(xg**2 + yg**2)
    idou = 0
    if kyori < r:
        ans += 1
    while kyori > idou:
        ans += 1
        idou += r
    
    print(int(ans))
hosuu()