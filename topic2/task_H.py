# H. Наибольшее произведение трех чисел

seq = list(map(int, input().split()))

max1 = -10**9
max2 = -10**9
max3 = -10**9
min1 = 10**9
min2 = 10**9

for s in seq:
    if s >= max1:
        max3 = max2
        max2 = max1
        max1 = s
    elif s >= max2:
        max3 = max2
        max2 = s
    elif s >= max3:
        max3 = s
    if s <= min1:
        min2 = min1
        min1 = s
    elif s <= min2:
        min2 = s

if min1*min2*max1 > max1*max2*max3:
    print(min1, min2, max1)
else:
    print(max1, max2, max3)
