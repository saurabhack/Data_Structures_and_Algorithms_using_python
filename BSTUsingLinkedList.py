class BST:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None

def insertNode(treeNode,value):
    if treeNode.data==None:
        treeNode.data=value
        return
    if treeNode.data>=value:
        if treeNode.leftChild==None:
            treeNode.leftChild=BST(value)
            print("inserted at leftSide")
        else:
            insertNode(treeNode.leftChild,value)
    else:
        if treeNode.rightChild==None:
            treeNode.rightChild=BST(value)
            print("inserted at rightChild")
        else:
            insertNode(treeNode.rightChild,value)

searcTree=BST(None)
insertNode(searcTree,1)
insertNode(searcTree,2)
insertNode(searcTree,3)
insertNode(searcTree,4)

