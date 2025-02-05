class Queue:
    def __init__(self,size):
        self.size=size
        self.items=self.size*[None]
        self.start=-1
        self.top=-1
    def __str__(self):
        values=[str(x) for x in self.items]
        return ' '.join(values)
    def isEmpty(self):
        if self.start==-1:
            return True
        else:
            return False
    def isFull(self):
        if self.top+1==self.start:
            return True
        elif self.start==0 and self.top+1==self.size:
            return True
        else:
            return False
    def enqueue(self,value):
        if self.isFull():
            return "memory is full please remove some element which can make available space in memory"
        if self.top+1==self.size:
            self.top=0
        else:
            self.top+=1
            print("top value",self.top)
            if self.start==-1:
                self.start=0
            self.items[self.top]=value
        print(self.top)
    def dequeue(self):
        if self.isEmpty():
            return "memory is already empty !!"
        else: 
            firstElement=self.items[self.start]
            if self.start==self.top:
                self.start=-1
                self.top=-1
            elif self.size+1 == self.size:
                self.start=0
            self.items[self.start]=None
            self.start+=1
            return firstElement
    def peek(self):
        if self.isEmpty():
            return "no any element exists !"
        else:
            return self.items[self.start]
    def delete(self):
        if self.isEmpty():
            return "queue is already empty !"
        else:
            self.items=None
            self.items=self.size*[None]
            self.start=-1
            self.top=-1
        
data=Queue(4)
print(data.isEmpty())
print(data.enqueue(1))
print(data.enqueue(2))
print(data.enqueue(3))
print(data.enqueue(4))
print(data.dequeue())
print(data.dequeue())
data.delete()
print("peeked element of the queue is == ",data.peek())
print("data is here == ",data)