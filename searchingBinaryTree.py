import linkedList_queue as queue
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None
root=TreeNode(1)
first=TreeNode(2)
second=TreeNode(3)
third=TreeNode(4)
fourth=TreeNode(5)
sixth=TreeNode(6)
seventh=TreeNode(7)
root.leftChild=first
root.rightChild=second
first.leftChild=third
first.rightChild=fourth
second.leftChild=sixth
second.rightChild=seventh
def searching(rootNode,nodeValue):
    if not rootNode:
        return "Node is not exists"
    else:
        custom_queue=queue.Queue()
        custom_queue.enqueue(rootNode)
        while not custom_queue.isEmpty():
            root=custom_queue.dequeue()
            if root.value.data==nodeValue:
                return "Success"
            if root.value.leftChild is not None:
                custom_queue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                custom_queue.enqueue(root.value.rightChild)
        return "Not Found"

print(searching(first,10))                