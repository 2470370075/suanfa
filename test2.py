class Node():
    def __init__(self,elem):
        self.elem = elem
        self.lchild = None
        self.rchild = None


node1 = Node(1)

class Tree():

    sum = 0

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

    def xxorder(self,node):
        if node == None:
            return
        print(node.elem,end=' ')
        self.xxorder(node.lchild)
        if node.lchild != None and node.rchild != None:
            print(node.elem,end=' ')

        self.xxorder(node.rchild)
        if node.lchild != None and node.rchild != None:
            print(node.elem,end=' ')

    def plus(self,node,target):
        self.sum += node.elem
        if node.lchild != None:
            self.plus(node.lchild,target)
        if node.rchild != None:
            self.plus(node.rchild,target)
        if node.lchild == None and node.rchild == None:
            if self.sum == target:
                print(True,)
                return
        self.sum -= node.elem

    def leaf(self,node):
        if node == None:
            return 0
        if node.lchild != None:
            self.leaf(node.lchild)
        if node.rchild != None:
            self.leaf(node.rchild)
        if node.lchild == None and node.rchild == None:
            self.sum += 1
        return self.sum

    def inorder(self,node):
        if node == None:
            return
        self.inorder(node.lchild)
        print(node.elem,end=' ')
        self.inorder(node.rchild)

def equal(root1,root2):
    if root1 == None and root2 == None:
        return True
    if root1 == None and root2 != None:
        return False
    if root2 == None and root1 != None:
        return False
    if root1.elem == root2.elem:
        return equal(root1.lchild,root2.lchild) and equal(root1.rchild, root2.rchild)
    else:
        return False


def exchange(node):
    if node == None or node.lchild == None or node.rchild == None:
        return
    print(node.lchild.elem,node.rchild.elem)
    node.lchild.elem,node.rchild.elem = node.rchild.elem,node.lchild.elem
    exchange(node.lchild)
    exchange(node.rchild)

sum = 0
l = []


def balanced(node):
    global sum
    global l
    if node != None:
        sum += 1
    if node == None:
        return True
    if node.lchild == None and node.rchild == None:
        l.append(sum)
    if node.lchild != None:
        balanced(node.lchild)
    if node.rchild != None:
        balanced(node.rchild)
    sum -= 1
    if max(l)-min(l) > 1:
        return False
    else:
        return True

# class Solution:
#
#     def isBalanced(self, root):
#         self.res = True
#         def helper(root):
#             if not root:
#                 return 0
#             left = helper(root.lchild) + 1
#             right = helper(root.rchild) + 1
#             #print(right, left)
#             if abs(right - left) > 1:
#                 self.res = False
#             return max(left, right)
#         helper(root)
#         return self.res

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
# tree.plus(tree.root,8)
print('')
# print(tree.leaf(tree.root))
print('')

tree2 = Tree()
# tree2.add(0)
# tree2.add(1)
# tree2.add(2)
tree2.add(3)
tree2.add(4)
tree2.add(5)
# tree2.add(6)
# tree2.add(7)
# tree2.add(8)
# tree2.add(9)

# print(tree.root.elem)
#
# print(equal(tree.root,tree2.root))
# tree.inorder(tree.root)
# print('')
# # exchange(tree.root)
# tree.xxorder(tree.root)
solution = Solution()
print(tree.breath_travel())
print(solution.mergeTrees(tree.root,tree2.root))
print(tree.breath_travel())
