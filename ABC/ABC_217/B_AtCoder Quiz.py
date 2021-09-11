a = [input() for i in range(3)]

ans_list = ["ABC", "ARC", "AGC", "AHC"]
inp_list = []

for i in a:
    inp_list.append(i)
for ii in ans_list:
    if ii not in inp_list:
        print(ii)
