S = input()
r_list = [S[i] for i in range(len(S)) if i % 2 == 0]
l_list = [S[i] for i in range(len(S)) if i % 2 == 1]

print("No" if "L" in r_list or "R" in l_list else "Yes")
