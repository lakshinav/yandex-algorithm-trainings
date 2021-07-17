# H. Злые свинки

n = int(input())
res = 0
x = set()
for _ in range(n):
    xi, yi = tuple(map(int, input().split()))
    if xi not in x:
        res += 1
        x.add(xi)
print(res)
