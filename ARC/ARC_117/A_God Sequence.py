a, b = map(int,input().split())
ansa = []
ansb = []
wa = 0

for i in range(1, a+1):
    ansa.append(i)

for s in range(-b, 0):
    ansb.append(s)

c = abs(a-b)
flag = 0

if a < b:
    flag = 1

for i in range(c):
    if flag == 0:
        ansb[0] -= ansa[a-i-1]
    else:
        ansa[a-1] -= ansb[i]

ans = ansa + ansb
print(' '.join(map(str, ans)))