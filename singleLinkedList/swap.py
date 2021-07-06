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
    
    def swapData(self,x,y):
        if x == y:
            return
        prev_X = None
        tmp_X = self.head
        while tmp_X is not None and tmp_X.data != x:
            prev_X = tmp_X
            tmp_X = tmp_X.next
        
        prev_Y = None
        tmp_Y = self.head
        while tmp_Y is not None and tmp_Y.data != y:
            prev_Y = tmp_Y
            tmp_Y = tmp_Y.next
        
        if tmp_X == None or tmp_Y == None:
            return
        
        if prev_X != None:
            prev_X.next = tmp_Y
        else:
            self.head = tmp_Y
        
        if prev_Y != None:
            prev_Y.next = tmp_X
        else:
            self.head = tmp_X
        
        temp = tmp_X.next
        tmp_X.next = tmp_Y.next
        tmp_Y.next = temp
    
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

    llist.swapData(40,20)

    llist.printList()