N = int(input())
a_list = []  # 長さのリスト
b_list = []  # 速さのリスト
c_list = []  # 所用時間のリスト
for _ in range(N):
    A, B = map(int, input().split())
    a_list.append(A)
    b_list.append(B)
    c_list.append(A / B)
le = 0
sum_c = sum(c_list)

# 左の導火線から所要時間の合計を計算
for i in range(len(c_list)):
    le += c_list[i]
    # 合計の所要時間の半分を超える
    if sum_c / 2 <= le:
        pre_le = le - c_list[i]  # 一つ前までの所要時間の合計
        ri = sum(c_list[i + 1:])  # 右の火がどれくらいの時間燃えているか
        sa = abs(ri - pre_le) * b_list[i]  # 先に導火線iについた火がどれくらい進んでいるか

        # 左から見たぶつかる地点の計算（左の火が先にiについていた場合saを加算）
        ans = (a_list[i] - sa) / 2 + sum(a_list[:i])
        if pre_le < ri:
            ans += sa
        print(ans)
        exit()
