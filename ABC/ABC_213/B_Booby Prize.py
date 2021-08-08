_ = input()
a = list(map(int, input().split()))
a_so = sorted(a)

print(a.index(a_so[-2]) + 1)
