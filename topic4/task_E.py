# E. Пирамида

n = int(input())
d = {}
for _ in range(n):
    w,h = tuple(map(int, input().split()))
    if w not in d:
        d[w] = []
    d[w].append(h)
maxh = 0
for w in d:
    maxh += max(d[w])
print(maxh)
