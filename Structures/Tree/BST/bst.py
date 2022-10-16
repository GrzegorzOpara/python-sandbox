from random import randint


class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, curr_node):
        if data < curr_node.data:
            if curr_node.left_child == None:
                curr_node.left_child = Node(data)
            else:
                self._insert(data, curr_node.left_child)
        elif data > curr_node.data:
            if curr_node.right_child == None:
                curr_node.right_child = Node(data)
            else:
                self._insert(data, curr_node.rigth_child)
        else:
            print('Value already in tree!')
    
    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)
        else:
            print('None nodes in the tree!')

    def _print_tree(self, curr_node):
        if curr_node != None:
            self._print_tree(curr_node.left_child)
            print(str(curr_node.data))
            self._print_tree(curr_node.right_child)

def createTree(tree, num_elems=10, max_int=100):
    for elem in range(num_elems):
        cur_elem = randint(0, max_int)
        tree.insert(cur_elem)
    return tree

tree = Tree()
tree = createTree(tree)
tree.print_tree()