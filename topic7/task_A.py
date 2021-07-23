START = -1
END = 1

n, m = tuple(map(int, input().split()))
eyes = []
for _ in range(m):
    tmp = tuple(map(int, input().split()))
    eyes.append((tmp[0], START))
    eyes.append((tmp[1], END))

eyes.sort()

watched = 0
l,r = 0,0
cnt = 0
for e in eyes:
    if e[1] == START:
        cnt += 1
    else:
        cnt -= 1
    if cnt == 0:
        watched += eyes[r][0] - eyes[l][0] + 1
        l = r + 1
    r += 1
    
print(n-watched)
