s = input()
a = [c for c in s]

cn_m = a.count("o")
cn_q = a.count("?")

pattern = (cn_m + cn_q) ** 4

if cn_m == 0:
    print(pattern)

elif cn_m == 1:
    print(pattern - cn_q ** 4)

elif cn_m == 2:
    ans = 14 + ((4 * 3 * 2 * cn_m) / 2) * cn_q + 4 * 3 * cn_q * cn_q
    print(int(ans))

# ３つのまるの数を用いた組み合わせ＋3つのまると一つのはてなを用いた組み合わせ
elif cn_m == 3:
    ans = (4 * 3 * 2 * cn_m) / 2 + 4 * 3 * 2 * 1 * cn_q
    print(int(ans))

elif cn_m == 4:
    print(24)

else:
    print(0)
