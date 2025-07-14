class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        cur = self.head

        new_node = Node(data)

        while cur.next != None:
            cur = cur.next

        cur.next = new_node

    def delete(self, target):
        cur = self.head

        prev = Node()

        while cur.data != target:
            if cur.next == None:
                return "not found in the list"
            prev = cur
            cur = cur.next

        if cur.next == None: # this only works if the element in question to delete the last one
            prev.next = None
        else:
            cur.data = cur.next.data
            cur.next = cur.next.next

    def print_ll(self):
        cur = self.head

        val = []
        cur = cur.next

        while cur:
            val.append(cur.data)
            cur = cur.next

        

        print(val)


ll = LinkedList()


ll.append(10)
ll.append(20)

ll.print_ll()

ll.delete(20)

ll.print_ll()
