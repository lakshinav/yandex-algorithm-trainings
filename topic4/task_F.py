# F. Продажи

d = {}
with open('input.txt', 'r', encoding = 'utf-8') as infile:
    for line in infile:
        name, good, qty = tuple(line.split())
        if name in d:
            if good in d[name]:
                d[name][good] += int(qty)
            else:
                d[name][good] = int(qty)
        else:
             d[name] = {}
             d[name][good] = int(qty)
names = sorted(d)
for n in names:
    print(n, ':', sep='')
    goods = sorted(d[n])
    for g in goods:
        print(g, d[n][g])
