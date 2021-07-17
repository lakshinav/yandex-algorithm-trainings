# C. Кубики

n,m = tuple(map(int, input().split()))
ann = []
bor = []
for _ in range(n):
    ann.append(int(input()))
for _ in range(m):
    bor.append(int(input()))

ann = set(ann)
bor = set(bor)
set1 = ann & bor
print(len(set1))
print(*sorted(set1))
set2 = ann - set1
print(len(set2))
print(*sorted(set2))
set3 = bor - set1
print(len(set3))
print(*sorted(set3))
