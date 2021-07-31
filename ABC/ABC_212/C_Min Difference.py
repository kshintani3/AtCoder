import bisect

_, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
ans = 1000000000

for aa in a:
    l = bisect.bisect_left(b, aa)  # 挿入できる最左インデックス
    r = bisect.bisect_right(b, aa)  # 挿入できる最右インデックス

    if l != r:  # lとrが異なるとき、aaと一致する値がある
        ans = 0
    elif l == m:  # l==m(=len(b))の時、aaはb内のどの値よりも大きいのでaa-max(b)が最小
        if ans > aa - b[-1]:
            ans = aa - b[-1]
    elif l == 0:  # l==0の時、aaはb内のどの値よりも小さいのでmin(b)-aaが最小
        if ans > b[0] - aa:
            ans = b[0] - aa
    else:  # 挿入される場所がlということはb[l]はb[l-1]<aa<b[l]となるので両サイドとの差の小さい方を採用
        c = min(abs(b[l] - aa), abs(b[l - 1] - aa))
        if ans > c:
            ans = c
print(ans)
