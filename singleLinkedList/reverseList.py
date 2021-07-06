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

    def reverseList(self):
        tmp = self.head
        prev = None
        while tmp is not None:
            next = tmp.next
            tmp.next = prev
            prev = tmp
            tmp = next
        self.head = prev
    
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

    llist.reverseList()

    llist.printList()