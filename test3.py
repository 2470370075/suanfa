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


def breath_travel(node):
    if node == None:
        return
    queue = []
    queue.append(node)
    while queue:
        cur_node = queue.pop(0)
        print(cur_node.elem,end=' ')

        if cur_node.lchild != None:
            queue.append(cur_node.lchild)
        if cur_node.rchild != None:
            queue.append(cur_node.rchild)

class Solution:
    l = []
    t3 = Tree()
    def mergeTrees(self,t1,t2):
        if t1 == None or t2 == None:
            return 0
        queue = [t1]
        queue2 = [t2]
        while queue and queue2:
            node1 = queue.pop(0)
            node2 = queue2.pop(0)
            ret = node1.elem + node2.elem
            print('xxxxxxxxxx')
            node1.elem = ret
            if node1.lchild != None and node2.lchild != None:
                queue.append(node1.lchild)
                queue2.append(node2.lchild)
            if node1.rchild != None and node2.rchild != None:
                queue.append(node1.rchild)
                queue2.append(node2.rchild)
        return t1

tree = Tree()
tree.add(1)

tree.add(3)
tree.add(2)
tree.add(5)
# tree.add(4)
# tree.add(5)
# tree.add(6)
# tree.add(7)
# tree.add(8)
# tree.add(9)
tree.breath_travel()
tree2 = Tree()
# tree2.add(0)
# tree2.add(1)
tree2.add(2)
tree2.add(1)
tree2.add(3)
tree2.add(0)
tree2.add(4)
tree2.add(0)
tree2.add(7)
# tree2.add(9)
print('')
tree.breath_travel()
solution = Solution()
print('')
tree.breath_travel()
# solution.mergeTrees(tree.root,tree2.root)
# tree.breath_travel()
breath_travel(solution.mergeTrees(tree.root,tree2.root))