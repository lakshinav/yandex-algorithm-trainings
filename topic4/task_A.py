# A. Словарь синонимов

n = int(input())
d1 = {}
d2 = {}
for _ in range(n):
    tmp = input().split()
    d1[tmp[0]] = tmp[1]
    d2[tmp[1]] = tmp[0]
word = input()
print(d1[word] if word in d1 else d2[word])
