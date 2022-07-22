import bisect

Q = int(input())
di = {}
s = []

for _ in range(Q):
    qi = list(map(int, input().split()))
    if qi[0] == 1:
        q1 = qi[1]
        if q1 in di:
            di[q1] += 1
        else:
            di[q1] = 1
            bisect.insort_left(s, q1)

    elif qi[0] == 2:
        q1, q2 = qi[1], qi[2]
        if q1 in di:
            di[q1] = max(0, di[q1] - q2)
            if di[q1] == 0:
                del di[q1]
                s.pop(bisect.bisect_left(s, q1))

    else:
        print(s[-1] - s[0])
