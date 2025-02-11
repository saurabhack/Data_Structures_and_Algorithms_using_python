class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkeLists:
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
    def peek(self):
        return self.head.data
    def pop(self):
        if self.head==None:
            return "queue is empty"
        self.head=self.head.next
    def display(self):
        current=self.head
        while current!=None:
            print(current.data,end="->")
            current=current.next
        print("Null")
link=LinkeLists()
link.push(1)
link.push(2)
link.push(3)
print(link.peek())
link.pop()
print(link.peek())
link.display()
