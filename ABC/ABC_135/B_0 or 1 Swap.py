N = int(input())
p = list(map(int, input().split()))
p_s = sorted(p)
cn = 0
for i in range(N):
    if p[i] != p_s[i]:
        cn += 1
print("YES" if cn <= 2 else "NO")
