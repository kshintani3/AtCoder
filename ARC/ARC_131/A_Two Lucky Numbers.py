A, B = input(), input()
if int(B) % 2 == 1:
    B += "2"
B = "0" + str(int(B) // 2)
print(A + B)
