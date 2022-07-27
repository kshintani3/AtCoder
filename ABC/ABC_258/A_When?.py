K = int(input())
if K >= 60:
    ans = str(2140 + K)
else:
    ans = str(2100 + K)

print(ans[0:2] + ":" + ans[2:])
