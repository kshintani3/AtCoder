N = int(input())
a = list(map(int, input().split()))

for i in range(N):
    if sum(a[N - 1 - i:]) >= 4:
        print(N - i)
        exit()
print(0)
