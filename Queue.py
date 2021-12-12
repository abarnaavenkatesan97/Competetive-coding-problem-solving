class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LL:
    def __init__(self,head = None):
        self.head = head
        self.tail = None
    def push(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.tail.next
            self.tail.next = newnode
            self.tail = newnode
    def pop(self):
        self.head = self.head.next
    def printer(self):
        temp = self.head
        while(temp):
            print(temp.data,end="->")
            temp = temp.next
        print("\n")
Momo = LL()
for i in range(1,4):
    Momo.push(i)
    Momo.printer()
for i in range(1,4):
    Momo.pop()
    Momo.printer()