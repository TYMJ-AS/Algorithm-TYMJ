import copy
N, K = map(int, input().split())

K_onebone = copy.deepcopy(K)
N_onebone = copy.deepcopy(N)
yoseputh = list(range(1, N+1))
cnt = 0
buffer_list = []
print(yoseputh)

while N != 0:

    print(f"K : {K}") # 0
    print(f"N : {N}") # 3
    print(yoseputh.pop(K - 1)) # 5
    N -= 1 # 2
    K -= 1 # -1
    if K + K_onebone > N:
        K = (K + K_onebone) % N
    else:
        K = K + K_onebone
    #buffer_list.append(yoseputh.pop(pop_num))


print(buffer_list)
# 아직 덜 풀었습니다 ㅠㅠ