class BinaryTreeUsingList:
    def __init__(self,size):
        self.binary=size*[None]
        self.maxSize=size
        self.lastIndex=0
    def insert(self,data):
        if self.lastIndex+1==self.maxSize:
            return "Tree is full"
        self.binary[self.lastIndex+1]=data
        self.lastIndex+=1
        return "successfully inserted!!"
    def searching(self,value):
        if self.lastIndex==0:
            return "tree is empty"
        for i in range(len(self.binary)):
            if self.binary[i]==value:
                return True
        return False
    def preOrderTraversal(self,index):
        if index>self.lastIndex:
            return
        print(self.binary[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2+1)
    def inOrderTraversal(self,index):
        if index>self.lastIndex:
            return
        self.preOrderTraversal(index*2)
        print(self.binary[index])
        self.preOrderTraversal(index*2+1)
    def postOrderTraversal(self,index):
        if index>self.lastIndex:
            return
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2+1)
        print(self.binary[index])
    def levelOrderTraversal(self,index):
        for i in range(index,self.lastIndex+1):
            print(self.binary[i])
    def deleteNode(self,value):
        if self.lastIndex==0:
            return "There is not any node to delete"
        for i in range(1,self.lastIndex+1):
            if self.binary[i]==value:
                self.binary[i]=self.binary[self.lastIndex]
                self.binary[self.lastIndex]=None
                self.lastIndex-=1
                return "the node has been successfully deleted"
    def deleteEntireTree(self):
        self.binary=None
        self.lastIndex=0
        
customTree=BinaryTreeUsingList(5)
customTree.insert(1)
customTree.insert(2)
customTree.insert(3)
customTree.insert(4)
customTree.inOrderTraversal(1)
print("level order traversal")
customTree.levelOrderTraversal(1)
customTree.deleteNode(3)
customTree.levelOrderTraversal(1)