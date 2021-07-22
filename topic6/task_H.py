# H. Провода

n,k = tuple(map(int, input().split()))
wires = []
for _ in range(n):
    wires.append(int(input()))

def rbinsearch(l,r,check,k,wires):
    while l != r:
        mid = (l+r+1)//2
        if check(mid, k, wires):
            r = mid - 1
        else:
            l = mid
    return l

def check(max_wires_len, k, wires):
    wires_cnt = 0
    for w in wires:
        wires_cnt += w//max_wires_len
    return wires_cnt < k

print(rbinsearch(1,10**7,check, k, wires)) if sum(wires) >= k else print(0)
