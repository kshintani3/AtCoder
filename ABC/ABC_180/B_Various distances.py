_ = int(input())
a = list(map(float, input().split()))
a = [int(abs(i)) for i in a]
b = [i * i for i in a]

print(sum(a))
print(sum(b) ** 0.5)
print(max(a))
