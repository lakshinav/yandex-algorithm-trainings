n,k = tuple(map(int, input().split()))
seq = list(map(int, input().split()))

cnt = 0
l,r = 0,1
tmp_sum = seq[l]
while l < n and r < n:
    if tmp_sum == k:
        cnt += 1
        tmp_sum -= seq[l]
        l += 1
        r += 1 if r < l else 0
    elif tmp_sum < k:
        tmp_sum += seq[r]
        r += 1
    elif tmp_sum > k:
        tmp_sum -= seq[l]
        l += 1

while l < n:
    if tmp_sum == k:
        cnt += 1
    tmp_sum -= seq[l]
    l += 1
    
print(cnt)
