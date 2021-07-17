# B. Определить вид последовательности

seq = []
while True:
    tmp = int(input())
    if tmp == -2000000000:
        break
    seq.append(tmp)

is_const = True
is_decrease = True
is_increase = True
is_weak_increase = True
is_weak_decrease = True

for i in range(1,len(seq)):
    if seq[i-1] == seq[i]:
        is_const *= True # CONSTANT 
    else:
        is_const *= False
    if seq[i-1] > seq[i]:
        is_decrease *= True # DESCENDING 
    else:
        is_decrease *= False
    if seq[i-1] < seq[i]: 
        is_increase *= True # ASCENDING
    else:
        is_increase *= False
    if seq[i-1] <= seq[i]:
        is_weak_increase *= True # WEAKLY ASCENDING
    else:
        is_weak_increase *= False
    if seq[i-1] >= seq[i]:
        is_weak_decrease *= True # WEAKLY DESCENDING
    else:
        is_weak_decrease *= False

if is_const:
    print('CONSTANT')
elif is_decrease:
    print('DESCENDING')
elif is_increase:
    print('ASCENDING')
elif is_weak_increase:
    print('WEAKLY ASCENDING')
elif is_weak_decrease:
    print('WEAKLY DESCENDING')
else:
    print('RANDOM')
