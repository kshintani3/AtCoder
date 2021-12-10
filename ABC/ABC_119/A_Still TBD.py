Y, M, _ = map(int, input().split("/"))
if (Y == 2019 and M < 5) or Y < 2019:
    print("Heisei")
else:
    print("TBD")
