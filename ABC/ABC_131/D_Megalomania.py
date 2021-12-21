N = int(input())

li = []
for _ in range(N):
    li.append(list(map(int, input().split())))

li = sorted(li, key=lambda x: x[1])

total = 0
for a, b in li:
    total += a
    if total > b:
        print("No")
        exit()
print("Yes")
