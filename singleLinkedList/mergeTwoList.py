class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def pushData(self,new_data):
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

def MergeList(headA, headB):
    dummy = Node(0)

    tail = dummy

    while True:
        if headA == None:
            tail = headB
            break
        if headB == None:
            tail = headA
            break
        
        if headA.data <= headB.data:
            tail.next = headA
            headA = headA.next
        else:
            tail.next = headB
            headB = headB.next
        tail = tail.next
    
    return dummy.next



if __name__ == "__main__":
    llist1 = LinkedList()
    llist2 = LinkedList()

    llist1.pushData(50)
    llist1.pushData(40)
    llist1.pushData(30)
    llist1.pushData(20)

    print("List-1")
    llist1.printList()

    llist2.pushData(65)
    llist2.pushData(55)
    llist2.pushData(45)
    llist2.pushData(35)

    print("List-2")
    llist2.printList()

    llist1.haed = MergeList(llist1.head,llist2.head)

    llist1.printList()
