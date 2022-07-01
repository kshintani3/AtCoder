N = int(input())
si = "1"
x = 1
for i in range(N - 1):
    x += 1
    si = si + " " + str(x) + " " + si
print(si)
