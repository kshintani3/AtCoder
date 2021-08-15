N = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

m0 = t[0]
s_sum = 0

for i in range(1, N):
    s_sum += s[-i]
    m0 = min(m0, t[-i] + s_sum)
print(m0)

for i in range(1, N):
    m0 += s[i - 1]
    m0 = min(m0, t[i])
    print(min(m0, t[i]))
