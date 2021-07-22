# B. Глубина добавляемых элементов
# реализация через менеджер памяти, как на лекции

def initmemory(maxn):
    memory = []
    for i in range(maxn):
        memory.append([0, i+1, 0]) # root, left son (smaller), right son (greater)
    return [memory, 0] # memory array, pointer to the first free element

def newnode(memstruct):
    memory, firstfree = memstruct
    memstruct[1] = memory[firstfree][1]
    return firstfree

def delnode(memstruct, index):
    memory, firstfree = memstruct
    memory[index][1] = firstfree
    memstruct[1] = index


def createandfillnode(memstruct, key):
    index = newnode(memstruct)
    memstruct[0][index][0] = key # value
    memstruct[0][index][1] = -1 # left son; index, not value!
    memstruct[0][index][2] = -1 # right son; index, not value!
    return index

def add(memstruct, root, x):
    key = memstruct[0][root][0]
    if x < key:
        left = memstruct[0][root][1]
        if left == -1:
            memstruct[0][root][1] = createandfillnode(memstruct, x)
        else:
            add(memstruct, left, x)  
    elif x > key:
        right = memstruct[0][root][2]
        if right == -1:
            memstruct[0][root][2] = createandfillnode(memstruct, x)
        else:
            add(memstruct, right, x)

def find_tree_depth(memstruct):
    stack = [(0, [0])]
    end = [-1, -1]
    res = []
    depth = []
    while stack:
        cur, route = stack.pop()
        depth.append((cur, len(route)))
        if memstruct[0][cur][1:] == end:
            res.append(route) 
        else:
            for node in memstruct[0][cur][1:]:
                if node == -1:
                    continue
                stack.append((node, route + [node]))
    return depth

seq = list(map(int, input().split()))

memstruct = initmemory(len(seq)-1)
root = createandfillnode(memstruct, seq[0])
i = 1
while seq[i] > 0:
    add(memstruct, root, seq[i])
    i += 1

for ind,d in sorted(find_tree_depth(memstruct)):
    print(d, end = ' ')
