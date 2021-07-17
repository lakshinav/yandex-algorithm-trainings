# G. Детали

N, K, M = tuple(map(int, input().split()))
if K < M:
    print(0)
else:
    rest = 300
    M_final = 0 # detail quantity
    while rest >= K:
        rest = 0
        K_qnt = N//K
        rest += N%K
        M_qnt = (K//M)*K_qnt
        M_final += M_qnt
        rest += (K%M)*K_qnt

        N = rest
    print(M_final)
