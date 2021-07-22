# G. Вывод веток

class BinSearchTree:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def insert_node(self, value):
        if self.value is None: # for this: bst = BinSearchTree(None)
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
        elif value > prev_node.value:
            prev_node.right = new_node
        return self
   
    
    def traverseSticks(self):
        if self.left:
            self.left.traverseSticks()
        if (self.right and not self.left) or (not self.right and self.left):
            print(self.value)
        if self.right:
            self.right.traverseSticks()             
  


seq = list(map(int, input().split()))[:-1]

bst = BinSearchTree()
for s in seq:
    bst.insert_node(s) 
bst.traverseSticks()
