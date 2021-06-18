import math
n = int(input())
li = [input().split() for l in range(2)]

x0 = float(li[0][0])
y0 = float(li[0][1])
xg = float(li[1][0])
yg = float(li[1][1])

hann = math.sqrt(x0*xg + y0*yg)

naikaku = (180 * (n-2)) / n

zeroiti = hann * math.cos(naikaku/2)
xlin = zeroiti * math.sin(naikaku/2)
ylin = zeroiti * math.cos(naikaku/2)

x1 = x0 - xlin
y1 = y0 - ylin

print(x1,end=" ")
print(y1)