# B. Номер появления слова

import re
res = []
d = {}
with open('input.txt', 'r', encoding = 'utf-8') as infile:
    text = re.split(r'[ \n]+', infile.read().strip())
for word in text:
    word = word.strip()
    if word in d:
        d[word] += 1
        res.append(d[word])
    else:
        d[word] = 0
        res.append(0)
if text != ['']:
    print(*res)
