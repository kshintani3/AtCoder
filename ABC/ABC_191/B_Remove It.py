N, X = map(int, input().split())
a = list(map(int, input().split()))

ans = [i for i in a if i != X]

print(*ans)
