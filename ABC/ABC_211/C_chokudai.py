import numpy as np

a = list(input())
chokudai = ["c", "h", "o", "k", "u", "d", "a", "i"]
pos = {}
flag = False

for i in range(8):
    pos[chokudai[i]] = (np.where(np.array(a) == chokudai[i])[0])
    if len(pos[chokudai[i]]) < 1:
        flag = True
if flag:
    print(0)
else:
    for j in range(7):
        pos[chokudai[j]] = [s for s in pos[chokudai[j]] if s < max(pos[chokudai[j + 1]])]
        if len(pos[chokudai[j]]) < 1:
            flag = True

    if flag:
        print(0)
    else:
        cnt_dict = {}
        chokudai.reverse()
        for s in range(1, 8):
            cnt = []
            if s == 1:
                for k in pos[chokudai[s]]:
                    cnt_dict[k] = sum(1 for x in pos[chokudai[s - 1]] if k < x)
            else:
                for k in pos[chokudai[s]]:
                    cnt_dict[k] = sum(cnt_dict[x] for x in pos[chokudai[s - 1]] if k < x)
        ans = 0
        for i in pos["c"]:
            ans += cnt_dict[i]
        print(ans)
