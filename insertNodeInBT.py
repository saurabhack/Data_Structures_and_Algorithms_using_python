import linkedList_queue as queue
class treeNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None
firstNode=treeNode(1)
secondNode=treeNode("management")
firstNode.leftChild=secondNode
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        custom_queue=queue.Queue()
        custom_queue.enqueue(rootNode)
        while not custom_queue.isEmpty():
            root=custom_queue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                custom_queue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                custom_queue.enqueue(root.value.rightChild)
def insertNode(rootNode,newNode):
    if not rootNode:
        rootNode=newNode
    else:
        customQueue=queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root=customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild=newNode
                return "Successfully inserted"
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild=newNode
                return "Successfully inserted"
newNode=treeNode('development')
print(insertNode(firstNode,newNode))
levelOrderTraversal(firstNode)