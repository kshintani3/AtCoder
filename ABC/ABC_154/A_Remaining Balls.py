S, T = input().split()
a = list(map(int, input().split()))
s_dic = {S: 0, T: 1}
a[s_dic[input()]] -= 1
print(*a)
