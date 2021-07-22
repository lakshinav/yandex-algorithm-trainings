# C. Второй максимум
# реализация через класс, не как на лекции
# inspired by https://github.com/Yankovsky/yandex-algos-training/blob/master/hw8/a.py

class BinSearchTree:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def insert_node(self, value):
        if self.value is None: # for this initialization: bst = BinSearchTree()
            self.value = value
            return self

        prev_node = None
        cur_node = self
        while cur_node is not None:
            prev_node = cur_node
            if value < cur_node.value:
                cur_node = cur_node.left
            elif value > cur_node.value:
                cur_node = cur_node.right
            else:
                return self

        new_node = BinSearchTree(value=value)
        
        if value < prev_node.value:
            prev_node.left = new_node
        else:
            prev_node.right = new_node
        return self

    def traverseInOrder_2max(self, ordered_seq):
        if self.right:
            self.right.traverseInOrder_2max(ordered_seq)
            if len(ordered_seq) >= 2:
                return ordered_seq[1]
        if self:
            ordered_seq.append(self.value)
            if len(ordered_seq) >= 2:
                return ordered_seq[1]
        if self.left:
            self.left.traverseInOrder_2max(ordered_seq)
            if len(ordered_seq) >= 2:
                return ordered_seq[1]


seq = list(map(int, input().split()))

bst = BinSearchTree()
for s in seq[:-1]:
    bst.insert_node(s) 

print(bst.traverseInOrder_2max(ordered_seq=[]))
