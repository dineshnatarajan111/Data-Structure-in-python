class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
    
    def push(self,data):
        new_node = Node(data)
        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return
        self.head = new_node
    
    def pushAfterKey(self,key,data):
        if self.head is None:
            print("List is empty")
            return
        new_node = Node(data)
        tmp = self.head
        while tmp is not None:
            if tmp.data == key:
                temp = tmp.next
                tmp.next = new_node
                new_node.prev = tmp
                new_node.next = temp
                return
            tmp = tmp.next

        print(key,"data not found")

    def pushBeforeKey(self,key,data):
        if self.head is None:
            print("List is empty")
            return
        tmp = self.head
        new_node = Node(data)
        while tmp is not None:
            if tmp.data == key:
                temp = tmp.prev
                tmp.prev.next = new_node
                new_node.prev = temp
                new_node.next = tmp
                return
            tmp = tmp.next
    
    def appendData(self,data):
        if self.head is None:
            self.head = Node(data)
            return
        tmp = self.head
        while tmp.next is not None:
            tmp = tmp.next
        new_node = Node(data)
        tmp.next = new_node
        new_node.prev = tmp

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

    list.push(10)
    list.push(20)
    list.push(30)
    list.push(40)

    list.printList()

    list.pushAfterKey(10, 8)
    list.pushAfterKey(12, 11)

    list.printList()

    list.pushBeforeKey(10, 15)
    list.pushBeforeKey(12, 13)

    list.printList()

    list.appendData(7)
    list.appendData(5)

    list.printList()