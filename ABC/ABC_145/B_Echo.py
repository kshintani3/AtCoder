N = int(input())
S = input()
print("Yes" if S[:N // 2] == S[N // 2:] and N % 2 == 0 else "No")
