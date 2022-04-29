N = int(input())
a = list(map(int, input().split()))

li = []
cn = 0

for i in range(N):
    if len(li) == 0 or li[-1][0] != a[i]:
        li.append([a[i], 1])
    else:
        li[-1][1] += 1
    if len(li) > 0 and li[-1][0] == li[-1][1]:
        cn += li[-1][0]
        li.pop()
    print(i - cn + 1)
