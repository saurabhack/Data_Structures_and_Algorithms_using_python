class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedList:
    def __init__(self):
        self.head=None
    def push(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
            return
        current=self.head
        while current.next!=None:
            current=current.next
        current.next=newNode
    def tailNode(self):
        tail=None
        current=self.head
        while current.next!=None:
            current=current.next
        tail=current
        return tail
    def printLinkedLists(self):
        if self.head==None:
            print("linkedList is none no any data stored in this linked list")
            return 
        else:
            current=self.head
            while current!=None:
                print(current.data,end="->")
                current=current.next
            print("NULL")
    def reverseLinkedLists(self):
        current=self.head
        temp=Node(-1)
        first=Node(None)
        nextNode=current.next
        lastNode=self.tailNode()
        lastNode.next=temp
        first.next=current
        print(first)
    def removeCycle(self):
        slow=self.head
        fast=slow.next
        while slow!=fast:
            fast=fast.next.next
            slow=slow.next
        slow.next=None
ll=linkedList()
ll.push(1)
ll.push(2)               
ll.printLinkedLists() 
ll.reverseLinkedLists()
ll.printLinkedLists()
ll.reverseLinkedLists()
ll.printLinkedLists()