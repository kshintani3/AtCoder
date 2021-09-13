N = int(input())
a, b = [0] * N, [0] * N
for i in range(N):
    a[i], b[i] = map(int, input().split())

a_mi = min(a)
b_mi = min(b)
am = [i for i, ii in enumerate(a) if ii == a_mi]
bm = [i for i, ii in enumerate(b) if ii == b_mi]

if len(am) > 1 or len(bm) > 1:
    print(max(a_mi, b_mi))
elif am[0] != bm[0]:
    print(max(a_mi, b_mi))
else:
    a.remove(a_mi)
    b.remove(b_mi)
    a_mi2 = min(a)
    b_mi2 = min(b)
    print(min(max(a_mi, b_mi2), max(a_mi2, b_mi), a_mi + b_mi))
