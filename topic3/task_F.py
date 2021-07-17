# F. Инопланетный геном

genom1 = input()
genom2 = input()

pairs = {}
for i in range(1, len(genom1)):
    tmp = genom1[i-1:i+1]
    if tmp in pairs:
        pairs[tmp] += 1
    else:
        pairs[tmp] = 1
res = 0
pairs2 = set()
for i in range(1, len(genom2)):
    pairs2.add(genom2[i-1:i+1])
for p in pairs2:
    if p in pairs:
        res += pairs[p]
print(res)
