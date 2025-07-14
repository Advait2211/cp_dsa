class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)

        cur = self.head

        while cur.next:
            cur = cur.next

        cur.next = new_node

    def delete(self, data):
        cur = self.head

        while cur.data != data:

            if cur.next is None:
                return "target not found"
            
            cur = cur.next

        cur.data = cur.next.data
        cur.next = cur.next.next

    def length(self):
        cur = self.head
        lth = 0
        while cur:
            cur = cur.next
            lth += 1

        return lth
    

    def print_ll(self):
        val = []

        cur = self.head

        while cur.next:
            cur = cur.next
            val.append(cur.data)

        print(val)

ll = LinkedList()

ll.append(10)
ll.append(20)

ll.print_ll()

ll.delete(10)

ll.print_ll()

ll.delete(20)

ll.print_ll()




