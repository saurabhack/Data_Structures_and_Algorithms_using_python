class TreeNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None
root=TreeNode(1)
even=TreeNode(2)
odd=TreeNode(3)
even1=TreeNode(4)
even2=TreeNode(6)
odd1=TreeNode(5)
odd2=TreeNode(7)
root.leftChild=even
root.rightChild=odd
even.leftChild=even1
even.rightChild=even2
odd.leftChild=odd1
odd.rightChild=odd2
def postOrderTraversal(node):
    if not node:
        return
    postOrderTraversal(node.leftChild)
    postOrderTraversal(node.rightChild)
    print(node.data)
postOrderTraversal(root)