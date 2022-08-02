S = input()
T = input()

i, j, x = 0, 0, ''
while i < len(T):
    sc, tc = 0, 0
    x = T[i]
    while i != len(T) and x == T[i]:
        tc += 1
        i += 1
    while j != len(S) and x == S[j]:
        sc += 1
        j += 1
    if (sc == 1 and tc == 1) or 1 < sc <= tc:
        continue
    else:
        print("No")
        exit()
print("Yes")
