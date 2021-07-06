class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def pushdata(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def popData(self):
        tmp = self.head
        if tmp is not None:
            self.head = tmp.next
    def popDataKey(self,key):
        tmp = self.head
        if tmp is not None:
            if tmp.data == key:
                self.head = tmp.next
                return
        while tmp is not None:
            if tmp.next.data == key:
                tmp.next = tmp.next.next
                break
            tmp = tmp.next

    def printList(self):
        tmp = self.head
        while(tmp):
            print(tmp.data,end="")
            if tmp.next:
                print("->",end="")
            tmp = tmp.next
        print()

if __name__ == "__main__":
    llist = LinkedList()

    llist.pushdata(20)
    llist.pushdata(10)
    llist.pushdata(40)
    llist.pushdata(50)

    llist.printList()

    llist.popData()

    llist.printList()

    llist.popDataKey(10)

    llist.printList()