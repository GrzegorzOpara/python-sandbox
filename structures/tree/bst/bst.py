from random import randint


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None

    def insert(self, data):
        if not self.data:
            self.data = data
            return 
        
        if self.data == data:
            return

        if self.data < data:
            if not self.right_child:
                self.right_child = Node(data)
            else:
                self.right_child.insert(data)
        elif self.data > data:
            if not self.left_child:
                self.left_child = Node(data)
            else:
                self.left_child.insert(data)
        else:
            return
    
def createTree(num_elems=100, max_int=100):
    tree = Node()
    for elem in range(num_elems):
        cur_elem = randint(0, max_int)
        print(cur_elem)
        tree.insert(cur_elem)
    return tree

tree = createTree()
# tree.print_tree()