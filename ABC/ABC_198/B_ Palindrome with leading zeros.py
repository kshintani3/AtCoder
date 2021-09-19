N = input()
N = N.strip("0")

if N == N[::-1]:
    print("Yes")
else:
    print("No")
