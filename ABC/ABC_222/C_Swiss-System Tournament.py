N, M = map(int, input().split())
a = [list(map(int, list(input()))) for i in range(N)]
rank = [range(N)]
# じゃんけんの組み合わせ９パターン
judge = {"GG": (1, 1), }
# 試合後に何点入ったか記録して、valueでソートした順番をrankに格納
wl = {}

for i in range(M):
    for j in range(0, N, 2):
        game = a[j][i] + a[j + 1][i]
