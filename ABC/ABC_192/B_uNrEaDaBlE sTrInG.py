S = input()
lo_list = [S[i] for i in range(len(S)) if i % 2 == 0]
up_list = [S[i] for i in range(len(S)) if i % 2 == 1]

# listの要素が0である時の対処
lo_list.append("a")
up_list.append("A")

lo = ''.join(lo_list)
up = ''.join(up_list)

if lo.islower() and up.isupper():
    print("Yes")
else:
    print("No")
