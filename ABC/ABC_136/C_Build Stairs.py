N = int(input())
h = list(map(int, input().split()))

h_m = 0
for i in h:
    if h_m - i > 0:
        print("No")
        exit()
    h_m = max(h_m, i - 1)
print("Yes")
