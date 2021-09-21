import sys

N = int(input())
a = [str(input()) for i in range(N)]
a = set(a)

for aa in a:
    if "!" + aa in a:
        print(aa)
        sys.exit()
print("satisfiable")
