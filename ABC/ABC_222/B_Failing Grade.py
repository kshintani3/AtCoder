N, P = map(int, input().split())
a = list(map(int, input().split()))
ans = [i for i in a if i < P]
print(len(ans))
