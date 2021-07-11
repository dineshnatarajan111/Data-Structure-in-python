class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self,new_data):
        tmp = Node(new_data)
        tmp.next = self.head
        self.head = tmp
    
    def printList(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.data, end="")
            if tmp.next is not None:
                print("->", end = "")
            tmp = tmp.next
        print()
    
    def rotate(self, k):
        if k == 0:
            return
        current = self.head

        count = 1

        while count<k and current.next is not None:
            current = current.next
            count += 1
        tmp = current.next
        head = current.next
        current.next = None
        while tmp.next is not None:
            tmp = tmp.next
        tmp.next = self.head
        self.head = head
        

if __name__ == "__main__":
    lst = LinkedList()

    lst.push(60)
    lst.push(50)
    lst.push(40)
    lst.push(30)
    lst.push(20)
    lst.push(10)

    lst.printList()

    lst.rotate(4)

    lst.printList()