class Node():
    def __init__(self, elem):
        self.val= elem
        self.left = None
        self.right = None


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5


def travel(node):
    l = []
    ret = []
    while l or node:
        if node:
            l.append(node)
            node = node.left
        else:
            node = l.pop()
            ret.append(node.val)
            node = node.right
    return ret


def preOrderTravese(node):
    stack = [node]
    while len(stack) > 0:
        print(node.val)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
        node = stack.pop()


print(travel(node1))
preOrderTravese(node1)
