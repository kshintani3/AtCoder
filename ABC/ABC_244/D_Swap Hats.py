S = input()
T = input()

ans = [S[i] == T[i] for i in range(0, 5, 2)]

print("No" if sum(ans) == 1 else "Yes")
