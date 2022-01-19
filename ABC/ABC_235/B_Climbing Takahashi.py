_ = input()
h = list(map(int, input().split()))

ans = 0
for i in h:
    if ans < i:
        ans = i
    else:
        break
print(ans)
