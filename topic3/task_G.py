# G. Черепахи

n = int(input())
res = 0
a = set()
for _ in range(n):
    ai, bi = tuple(map(int, input().split()))
    if ai>=0 and bi >=0 and ai not in a and ai+bi == n-1:
        res += 1
        a.add(ai)
print(res)
