a = list(map(int, input().split()))
a.sort(reverse=True)
print(sum([abs(a[i + 1] - a[i]) for i in range(2)]))
