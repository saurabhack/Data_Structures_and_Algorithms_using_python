#queue datastructure using python

class queue:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        if self.items==[]:
            return True
        else :
            return False
    def enqueue(self,value):
        self.items.append(value)
    def dequeue(self):
        if(self.isEmpty()):
            return "list is empty !!"
        else:
            return self.items.pop(0)
    def delete(self):
        if(self.isEmpty()):
            return "list is already empty"
        self.items=None
    def peek(self):
        return self.items[0]
    def display(self):
        return self.items
    
custome_queue=queue()
custome_queue.enqueue(1)
custome_queue.enqueue(2)
custome_queue.enqueue(3)
custome_queue.enqueue(4)
custome_queue.dequeue()
print(custome_queue.peek())
print(custome_queue.display())
