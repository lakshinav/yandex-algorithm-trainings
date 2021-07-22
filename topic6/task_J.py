# J. Медиана объединения

N, L = tuple(map(int, input().split()))
seq = []
for i in range(N):
    seq.append(tuple(map(int, input().split())))

def merge_seq(seq1, seq2, L):
    i1,i2 = 0,0
    cnt = 0
    while i1 < L and i2 < L and cnt < L:
        if seq1[i1] >= seq2[i2]:
            i2 += 1
            flag1 = False
        else:
            i1 += 1
            flag1 = True
        cnt += 1
    return seq1[i1-1] if flag1 else seq2[i2-1]

for j1 in range(N):
    for j2 in range(j1+1, N):
            print(merge_seq(seq[j1], seq[j2], L))
