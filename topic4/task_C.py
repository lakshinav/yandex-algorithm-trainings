# C. Самое частое слово

import sys
text = sys.stdin.read().split()


d = {}
for word in text:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

maxval = 0
for k,v in d.items():
    if v > maxval:
       maxval = v
       maxkey = k
    elif v == maxval and k < maxkey:
        maxkey = k
print(maxkey)
