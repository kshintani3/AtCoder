N, X = map(int, input().split())
l = list(map(int, input().split()))
ans = 1
y = 0

for i in l:
    y += i
    if y > X:
        print(ans)
        exit()
    ans += 1
print(ans)
