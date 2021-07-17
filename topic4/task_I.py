# I. Контрольная по ударениям

n = int(input())
dictionary = {}
for _ in range(n):
    word = input()
    wordLower = word.lower()
    if wordLower not in dictionary:
        dictionary[wordLower] = []
    dictionary[wordLower].append(word)

petya = input().split()
mistakes = 0
for word in petya:
    wordLower = word.lower()
    if word.islower():
        mistakes += 1
    elif sum(1 for w in word if w.isupper()) > 1:
        mistakes += 1
    elif wordLower in dictionary and word not in dictionary[wordLower]:
        mistakes += 1
print(mistakes)
