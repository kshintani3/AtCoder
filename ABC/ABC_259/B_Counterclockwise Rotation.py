from math import *

a, b, d = map(int, input().split())
c = (a ** 2 + b ** 2) ** 0.5
dd = degrees(atan2(b, a))

print(c * cos(radians(d + dd)), c * sin(radians(d + dd)))
