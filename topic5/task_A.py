n = int(input())
shirts = list(map(int, input().split()))
m = int(input())
pants = list(map(int, input().split()))

sh, pan = 0,0
min_dist = 1e7+10
s_min = -1
p_min = -1
while sh < n and pan < m:
    cur_dist = abs(shirts[sh] - pants[pan])
    if cur_dist < min_dist:
        min_dist = cur_dist
        s_min = shirts[sh]
        p_min = pants[pan]
    if shirts[sh] > pants[pan]:
        pan += 1
    elif shirts[sh] < pants[pan]:
        sh += 1
    else:
        s_min = shirts[sh]
        p_min = pants[pan]
        break
print(s_min, p_min)
