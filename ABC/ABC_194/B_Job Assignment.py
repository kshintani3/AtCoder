N = int(input())
a, b = [0] * N, [0] * N
for i in range(N):
    a[i], b[i] = map(int, input().split())

a_mi = min(a)
b_mi = min(b)
am = [i for i, x in enumerate(a) if x == a_mi]
bm = [i for i, x in enumerate(b) if x == b_mi]

# どちらかの仕事で2人以上が最小時間で終えられる場合
if len(am) > 1 or len(bm) > 1:
    print(max(a_mi, b_mi))

# 最小の時間で終えられる人がどちらも一人ずつで同一人物でない場合
elif am[0] != bm[0]:
    print(max(a_mi, b_mi))

# 最小の時間で終えられる人がどちらも一人ずつで同一人物である場合
# 一人にどちらの仕事も割り当てるか、どちらかの仕事を別の人に割り当てるかを比較して決める。
else:
    a.remove(a_mi)
    b.remove(b_mi)
    a_mi2 = min(a)
    b_mi2 = min(b)
    print(min(max(a_mi, b_mi2), max(a_mi2, b_mi), a_mi + b_mi))
