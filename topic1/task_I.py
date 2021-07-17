# I. Узник замка Иф

a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())
if (a <= d or b <= d or c <= d) and (a <= e or b <= e or c <= e):
    print('YES')
else:
    print('NO')
