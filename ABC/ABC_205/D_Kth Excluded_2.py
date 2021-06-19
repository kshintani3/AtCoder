# 16/21でTLE

def search(b, a):
    a_len = (len(a) + 1) // 2
    if len(a) == 1:
        return a[0]
    elif a[0] > b:
        return a[0]
    elif a[-1] < b:
        return a[-1]
    elif a[a_len] >= b:
        return search(b, a[0:a_len])
    else:
        return search(b, a[a_len:len(a)])


n, q = map(int, input().split())
a = list(map(int, input().split()))
a_list = [0]
for i in range(len(a)):
    a_list.append(a[i] - i - 1)
a.insert(0, 0)

for i in range(q):
    query = int(input())
    ind = search(query, a_list)
    ind_list = [i for i, x in enumerate(a_list) if x == ind]
    ind = ind_list[-1]
    if ind == 0:
        print(query)
    else:
        print(a[ind] + query - a_list[ind])
