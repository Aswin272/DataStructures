class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)

        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print(self):
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1

    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1

    def pop(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            pre = self.head
            while temp.next is not None:
                pre = temp
                temp = temp.next
            pre.next = None
            self.tail = pre
        self.length-=1

    def prepend(self,value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1


    def prepop(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
        self.length-=1

    
    def get(self,index):
        temp = self.head
        for _ in range(index):
            temp = temp.next
        
        return temp
    
    def set(self,index,value):
        temp = self.get(index)

        if temp:
            temp.value = value
        
    def insert(self,index,value):
        if index<0 or index>self.length:
            return None
        if index == 0:
            self.prepend(value)
            return True
        elif index == self.length:
            self.append(value)
            return True
        else:
            new_node = Node(value)
            prev = self.get(index-1)
            temp = prev.next
            prev.next = new_node
            new_node.next = temp
            self.length+=1

    def remove(self,index):
        if index<0 or index>self.length:
            return None
        if index == 0:
            self.prepop(index)
            return True
        elif index == self.length-1:
            self.pop()
            return True
        else:
            temp = self.get(index-1)
            temp.next = temp.next.next
            temp.next.next = None
            self.length-=1
        



    
l = LinkedList(2)
l.append(4)


l.insert(1,3)
l.remove(1)
l.print()



        