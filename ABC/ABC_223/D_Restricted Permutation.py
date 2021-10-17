N, M = map(int, input().split())
a_list = []
b_list = []
c_list = []
for _ in range(M):
    A, B = map(int, input().split())
    AB = str(A) + str(B)
    a_list.append(A)
    b_list.append(B)
    if AB not in c_list:
        print(-1)
        exit()
    c_list.append(AB)
