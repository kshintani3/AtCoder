import collections

n = int(input())
a = list(map(int, input().split()))

a_list = list(range(200000))
ans = 0


def find(v):
    if a_list[v] != v:
        a_list[v] = find(a_list[v])
    return a_list[v]


for i in range(n // 2):
    r, l = a[i], a[n - i - 1]
    r, l = find(r), find(l)
    if r != l:
        a_list[l] = r
        ans += 1

print(ans)
