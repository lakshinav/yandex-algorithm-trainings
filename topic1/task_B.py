# B. Треугольник

# хоть и сортируем, но сортируемых элементов всегда 3, поэтому O(1)

tri = []
for i in range(3):
    tri.append(int(input()))
tri.sort()
if tri[0]+tri[1] > tri[2]:
    print('YES')
else:
    print('NO')
