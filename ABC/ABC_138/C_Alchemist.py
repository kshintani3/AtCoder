N = int(input())
v = list(map(int, input().split()))
v_s = sorted(v)
a = v_s[0]
for i in v_s:
    a = (a + i) / 2
print(a)
