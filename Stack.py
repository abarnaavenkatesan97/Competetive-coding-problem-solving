class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class LL:
    def __init__(self,limit,head = None):
        self.head = head
        self.tail = None
        self.limit = limit
        self.count = 0
    def push(self,data):
        if self.count >= self.limit:
            print("Limit crossing")
            return
        newnode = Node(data)

        if self.tail is None:
            self.head = newnode
            self.tail = newnode
            self.count = self.count + 1
        else:
            newnode.prev = self.tail
            newnode.next = self.tail.next
            self.tail.next = newnode
            self.tail = newnode
            self.count += 1
    def pop(self):
        if self.count <= 1:
            self.head = None
            self.count = self.count - 1
            print("All elements are popped")
            return    
        temp = self.tail
        temp.prev.next = None
        self.tail = temp.prev
        self.count = self.count - 1
    def printer(self):
        temp = self.head
        while(temp):
            print(temp.data,end="->")
            temp = temp.next
        print("\n")
Momo = LL(3)
for i in range(1,5):
    Momo.push(i)
    Momo.printer()
for i in range(1,5):
    Momo.pop()
    Momo.printer()