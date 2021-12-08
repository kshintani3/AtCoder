a = []
for _ in range(5):
    a.append(int(input()))
k = int(input())
a.sort()
print(":(" if a[-1] - a[0] > k else "Yay!")
