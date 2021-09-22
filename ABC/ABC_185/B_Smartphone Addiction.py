N, M, T = map(int, input().split())
battery = N
last_b = 0

for _ in range(M):
    a, b = map(int, input().split())
    battery -= a - last_b
    if battery <= 0:
        print("No")
        exit()
    battery += b - a
    if battery > N:
        battery = N
    last_b = b
if battery - T + last_b <= 0:
    print("No")
else:
    print("Yes")
