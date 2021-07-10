n, b = map(int, input().split())
a = list(map(int, input().split()))

ans = sum(a) - n // 2

if ans > b:
    print("No")
else:
    print("Yes")
