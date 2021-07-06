class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def length(self):
        tmp = self.head
        lengthL = 0
        if tmp is not None:
            while tmp is not None:
                lengthL += 1
                tmp = tmp.next
        return lengthL
    

    def pushdata(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    

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

    length = llist.length()

    print(length)