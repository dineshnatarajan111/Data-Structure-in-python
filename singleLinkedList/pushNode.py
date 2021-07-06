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
    def insertAfterData(self,new_data,key):
        tmp = self.head
        if tmp is not None:
            if tmp.data == key:
                temp = tmp.next
                tmp.next = Node(new_data)
                tmp.next.next = temp
                return
            tmp = tmp.next
        while tmp is not None:
            if tmp.data == key:
                temp = tmp.next
                tmp.next = Node(new_data)
                tmp.next.next = temp
                break
            tmp = tmp.next
    def insertBeforeData(self,new_data,key):
        tmp = self.head
        if tmp is not None:
            if tmp.data == key:
                temp = Node(new_data)
                temp.next = tmp
                self.head = temp
                return
        while tmp is not None:
            if tmp.next.data == key:
                temp = tmp.next
                tmp.next = Node(new_data)
                tmp.next.next = temp
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

    llist.insertAfterData(30,10)

    llist.printList()

    llist.insertBeforeData(90,40)

    llist.printList()