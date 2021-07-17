# G. Наибольшее произведение двух чисел

seq = list(map(int, input().split()))

max1 = -10000
max2 = -10000
min1 = 10000
min2 = 10000
for s in seq:
    if s >= max1:
        max2 = max1
        max1 = s
    elif s >= max2:
        max2 = s
    if s <= min1:
        min2 = min1
        min1 = s
    elif s <= min2:
        min2 = s
if max1*max2 > min1*min2:
    print(min(max1, max2), max(max1, max2))
else:
    print(min(min1, min2), max(min1, min2))
