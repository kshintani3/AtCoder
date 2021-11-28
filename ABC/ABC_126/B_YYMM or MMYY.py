S = input()
a = int(S[:2])
b = int(S[2:])
if 0 < a <= 12 and 0 < b <= 12:
    print("AMBIGUOUS")
elif 0 < b <= 12:
    print("YYMM")
elif 0 < a <= 12:
    print("MMYY")
else:
    print("NA")
