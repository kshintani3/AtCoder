N = int(input())
S = [input() for _ in range(N)]
S_list = ["AC", "WA", "TLE", "RE"]
for i in S_list:
    print(i + " x " + str(S.count(i)))
