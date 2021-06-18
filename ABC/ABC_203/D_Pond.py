import itertools

n, k = map(int, input().split())

park = []
for i in range(n):
    park.append(list(map(int, input().split())))

ans_t = ((k ** 2 // 2) + 1) * (-1)
min_ans = 10 ** 9
plist = list(itertools.chain.from_iterable(park))

for i in range(n ** 2):
    m_list = []
    xi = i % n
    yi = i // n
    if (yi + k) > n:
        break
    if (xi + k) > n:
        continue
    else:
        for s in range(k):
            rix = i + s * n
            m_list.append(plist[rix:rix + k])
        m_list = list(itertools.chain.from_iterable(m_list))
        m_list.sort()
        if m_list[ans_t] < min_ans:
            min_ans = m_list[ans_t]

print(min_ans)
