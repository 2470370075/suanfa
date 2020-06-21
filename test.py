class Node():
    def __init__(self,elem):
        self.elem = elem
        self.lchild = None
        self.rchild = None


class Tree():

    def __init__(self):
        self.root = None

    def add(self,item):
        node = Node(item)
        if self.root == None:
            self.root = node
            return
        queue = []
        queue.append(self.root)
        while queue:             # 不可能取光啊
            cur_node = queue.pop(0)
            if cur_node.lchild == None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild == None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)


    def breath_travel(self):
        if self.root == None:
            return
        queue = []
        queue.append(self.root)
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem,end=' ')

            if cur_node.lchild != None:
                queue.append(cur_node.lchild)
            if cur_node.rchild != None:
                queue.append(cur_node.rchild)


    def preorder(self,node):
        if node == None:
            return
        print(node.elem,end=' ')
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def inorder(self,node):
        if node == None:
            return
        self.inorder(node.lchild)
        print(node.elem,end=' ')
        self.inorder(node.rchild)

    def postorder(self,node):
        if node == None:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.elem,end=' ')



tree = Tree()
tree.add(0)

tree.add(1)
tree.add(2)
tree.add(3)
tree.add(4)
tree.add(5)
tree.add(6)
tree.add(7)
tree.add(8)
tree.add(9)
tree.breath_travel()
print('')

tree.preorder(tree.root)
print('')
tree.inorder(tree.root)
print('')
tree.postorder(tree.root)

"""
   0
 1   2
3 4 5  6
789
"""

