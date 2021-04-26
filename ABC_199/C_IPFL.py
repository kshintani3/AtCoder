def main():
    n = int(input())
    s = [str(c) for c in input()]
    q = int(input())

    xy = [map(int, input().split()) for _ in range(q)]
    t,a,b = [list(i) for i in zip(*xy)]

    s0 = s[:n]
    s1 = s[n:]
    flag = 0

    for i in range(q):
        if t[i] == 1:
            ai = (a[i] + n)%n - 1
            bi = (b[i] + n)%n - 1
            if (b[i]<=n and flag == 0) or (n<a[i] and flag == 1):
                s0[ai],s0[bi] = s0[bi],s0[ai]
            elif (b[i]<=n and flag == 1) or (n<a[i] and flag == 0):
                s1[ai],s1[bi] = s1[bi],s1[ai]
            elif a[i] <= n < b[i]:
                if flag == 0:
                    s0[ai],s1[bi] = s1[bi],s0[ai]
                else:
                    s1[ai],s0[bi] = s0[bi],s1[ai]
        else:
            flag = (flag+1)%2
    if flag == 0:
        ans = s0 + s1
    else:
        ans = s1 + s0 
    print(''.join(map(str, ans)))

main()