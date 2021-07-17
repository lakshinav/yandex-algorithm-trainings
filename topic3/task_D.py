# D. Количество слов в тексте

with open('input.txt', 'r') as infile:
    text = infile.read()
text = text.split('\n')
words = []
for line in text:
    words += line.split()
print(len(set(words)))
