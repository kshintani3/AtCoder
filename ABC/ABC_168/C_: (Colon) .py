import math

A, B, H, M = map(int, input().split())

rad = abs(30 * (H + M / 60) - M * 6)
rad = min(rad, 360 - rad) * math.pi / 180

ans = ((A - B * math.cos(rad)) ** 2 + (B * math.sin(rad)) ** 2) ** 0.5

print(ans)
