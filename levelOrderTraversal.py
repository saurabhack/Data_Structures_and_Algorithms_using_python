import linkedList_queue as queue
class treeOrder:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None
first=treeOrder(1)
second=treeOrder(2)
second1=treeOrder(4)
second2=treeOrder(6)
third=treeOrder(3)
third1=treeOrder(5)
third2=treeOrder(7)
first.leftChild=second
first.rightChild=third
third.leftChild=third1
third.rightChild=third2
second.leftChild=second1
second.rightChild=second2
def preOrder(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrder(rootNode.leftChild)
    preOrder(rootNode.rightChild)
def levelOrderTraversal(rootNode):
    if not rootNode:
        return 
    else:
        customQueue=queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root=customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild) 
levelOrderTraversal(first)

