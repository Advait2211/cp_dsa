class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head

        while cur.next != None:
            cur = cur.next

        cur.next = new_node

    def length(self):
        cur = self.head
        lenth = 0

        while cur != None:
            lenth += 1
            cur = cur.next
        
        return lenth-1
    
    def delete(self, target):
        cur = self.head

        while cur.data != target:
            if cur.next is None:
                return "target not found"
            
            cur = cur.next

        cur.data = cur.next.data
        cur.next = cur.next.next

    def display(self):
        arr = []

        cur = self.head

        while cur.next != None:
            cur = cur.next
            arr.append(cur.data)

        print(arr)

ll = linkedlist()

ll.append(10)
ll.append(9)
ll.append(10)
ll.display()

print(ll.delete(1))

ll.display()

print(ll.length())
