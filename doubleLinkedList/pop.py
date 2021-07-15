class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
    
    def push(self,data):
        if self.head is None:
            self.head = Node(data)
            return
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    
    def popHead(self):
        if self.head is None:
            return
        tmp = self.head
        self.head = tmp.next
        tmp.next = None
        self.head.prev = None

    def popTail(self):
        if self.head is None:
            return
        tmp = self.head
        while tmp.next is not None:
            tmp = tmp.next
        tmp.prev.next = None
        tmp.prev = None
    
    def popElement(self, key):
        if self.head is None:
            return
        if self.head.data == key:
            self.head = self.head.next
            self.head.prev.next = None
            self.head.prev = None
            return
        tmp = self.head
        while tmp is not None:
            if tmp.data == key:
                if tmp.next is not None:
                    tmp.next.prev = tmp.prev
                    tmp.prev.next = tmp.next
                    return
                tmp.prev.next = None
                tmp.prev = None
                return
            tmp = tmp.next

    def printList(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.data, end = "")
            tmp = tmp.next
            if tmp is not None:
                print(" <-> ",end = "")
        print()

if __name__ == "__main__":
    list = DoubleLinkedList()

    list.push(40)
    list.push(30)
    list.push(20)
    list.push(10)

    list.printList()

    list.popHead()

    list.printList()

    list.popTail()

    list.printList()

    list.popElement(20)
    list.popElement(30)

    list.printList()