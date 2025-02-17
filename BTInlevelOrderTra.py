class treeNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None
root=treeNode(1)
first=treeNode(2)
second=treeNode(3)
first1=treeNode(4)
first2=treeNode(8)
second1=treeNode(6)
second2=treeNode(9)
root.leftChild=first
root.rightChild=second
first.leftChild=first1
first.rightChild=first2
second.leftChild=second1
second.rightChild=second2
def inLevelTraversel(node):
    if not node:
        return
    inLevelTraversel(node.leftChild)
    print(node.data)
    inLevelTraversel(node.rightChild)

inLevelTraversel(root)