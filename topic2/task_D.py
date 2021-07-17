# D. Больше своих соседей

seq = list(map(int, input().split()))
res = 0
if len(seq) > 2:
    for i in range(1,len(seq)-1):
        if seq[i] > seq[i-1] and seq[i] > seq[i+1]:
            res += 1
print(res)
