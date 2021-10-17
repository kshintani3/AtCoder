T_hp, T_at, A_hp, A_at = map(int, input().split())
if (T_hp - 1) // A_at < (A_hp - 1) // T_at:
    print("No")
else:
    print("Yes")
