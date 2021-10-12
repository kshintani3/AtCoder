N = int(input()) % 10
pon_list = [0, 1, 6, 8]
if N == 3:
    print("bon")
elif N in pon_list:
    print("pon")
else:
    print("hon")
