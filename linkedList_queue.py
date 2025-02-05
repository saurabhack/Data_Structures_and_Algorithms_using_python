#linkedList_queue implementations 
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        current=self.head
        while current:
            yield current
            current=current.next
class Queue:
    def __init__(self):
        self.linkedList=LinkedList()
    def __str__(self):
        values=[str(x) for x in self.linkedList]
        return ' '.join(values) 
    def isEmpty(self):
        if self.linkedList.head==None:
            return True
        else:
            return False
        
    def enqueue(self,value):
        newNode=Node(value)
        if self.linkedList.head==None:
            self.linkedList.head=newNode
            self.linkedList.tail=newNode
        else:
            self.linkedList.tail.next=newNode
            self.linkedList.tail=newNode
    def dequeue(self):
        if self.isEmpty():
            return "Queue is already empty !"
        else:
            tempNode=self.linkedList.head
            if self.linkedList.head==self.linkedList.tail:
                self.linkedList.head=None
                self.linkedList.tail=None
            else:
                self.linkedList.head=self.linkedList.next
            return tempNode
    def peek(self):
        return self.linkedList.head
    def delete(self):
        self.linkedList.head=None
        self.linkedList.tail=None
custom_queue=Queue()
custom_queue.enqueue(1)        
custom_queue.enqueue(2)        
custom_queue.enqueue(3)
custom_queue.dequeue()
print(custom_queue)        
