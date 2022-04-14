V = list(map(int, input().split()))
Vt = V[0] % (sum(V) - V[0])
if V[1] > Vt:
    print("F")
elif V[1] + V[2] > Vt:
    print("M")
else:
    print("T")
