N = int(input())
s = input()
Q = int(input())

s0, s1 = list(s[:N]), list(s[N:])
flag = 0

for i in range(Q):
    t, a0, b0 = map(int, input().split())
    if t == 1:
        a1 = (a0 + N) % N - 1
        b1 = (b0 + N) % N - 1

        if (b0 <= N and flag == 0) or (a0 > N and flag == 1):
            s0[a1], s0[b1] = s0[b1], s0[a1]
        elif (b0 <= N and flag == 1) or (a0 > N and flag == 0):
            s1[a1], s1[b1] = s1[b1], s1[a1]
        elif a0 <= N < b0:
            if flag == 0:
                s0[a1], s1[b1] = s1[b1], s0[a1]
            else:
                s1[a1], s0[b1] = s0[b1], s1[a1]
    else:
        flag = (flag + 1) % 2
if flag == 0:
    ans = s0 + s1
else:
    ans = s1 + s0
print(''.join(ans))
