class TreeNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None
root=TreeNode(1)
two=TreeNode(2)
two1=TreeNode(4)
two2=TreeNode(8)
three=TreeNode(3)
three1=TreeNode(6)
three2=TreeNode(9)
root.leftChild=two
root.rightChild=three
two.leftChild=two1
two.rightChild=two2
three.leftChild=three1
three.rightChild=three2
def preOrderTraversal(node):
    if not node:
        return 
    print(node.data)
    preOrderTraversal(node.leftChild)
    preOrderTraversal(node.rightChild)
preOrderTraversal(root)