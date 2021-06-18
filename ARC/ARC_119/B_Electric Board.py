N = int(input())
A = input()
B = input()
A_zero = [0 for ai in range(500000)]
B_zero = [0 for bi in range(500000)]
cn_A = 0
cn_B = 0
ans = 0

# 0が何番目にあるかを格納
for i in range(N):
    if A[i] == '0':
        A_zero[cn_A] = i
        cn_A += 1
    if B[i] == '0':
        B_zero[cn_B] = i
        cn_B += 1

if cn_A != cn_B:
    print("-1")
else:
    for i in range(cn_A):
        if A_zero[i] != B_zero[i]:
            ans += 1
    print(ans)
