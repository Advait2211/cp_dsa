class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None


class LL:
    def __init__(self):
        self.head = Node()

    def append(self, value):
        new_node = Node(value)

        cur = self.head

        while cur.next != None:
            cur = cur.next

        cur.next = new_node

    @property
    def length(self):
        l = 0

        cur = self.head

        while cur.next != None:
            cur = cur.next
            l += 1

        return l

    def print_ll(self):
        arr = []

        cur = self.head

        while cur.next != None:
            cur = cur.next
            arr.append(cur.data)

        print(arr)

    def delete(self, index):
        if index > self.length:
            return "fuck you"
        
        i = 0

        cur = self.head

        while i != index:
            cur = cur.next
            i += 1

        cur.data = cur.next.data
        cur.next = cur.next.next

        self.print_ll()

class DLL:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        cur = self.head

        new_node = Node(data)

        while cur.next != None:
            cur = cur.next

        cur.next = new_node

        new_node.prev = cur

    def print_dll(self):
        arr = []

        cur = self.head

        while cur.next != None:
            cur = cur.next
            arr.append(cur.data)

        print(arr)

    @property
    def length(self):
        l = 0

        cur = self.head

        while cur.next != None:
            cur = cur.next
            l += 1

        return l
    
    def delete(self, index):
        if index > self.length:
            return "fuck you"
        
        elif index == self.length:
            # deleting the last node, we need to cycle till second last one
            i = 0
            cur = self.head

            while i != index:
                i += 1
                cur = cur.next

            previous = cur.prev

            previous.next = None
            

        elif index == 0:
            # deleting the first node, prev will be set to head
            cur = self.head
            cur.next = cur.next.next
            next = cur.next
            next.prev = cur

        else:
            # deleting any middle node
            cur = self.head
            i = 0

            while i != index:
                i += 1
                cur = cur.next

            previous = cur.prev
            next = cur.next

            previous.next = next
            next.prev = previous

        self.print_dll()

class deque():
    def __init__(self):
        self.head = Node()

    def __str__(self):
        arr = []

        cur = self.head

        while cur.next != None:
            cur = cur.next
            arr.append(cur.data)

        return str(arr)

    def append_last(self, value):
        cur = self.head
        new_node = Node(value)

        while cur.next != None:
            cur = cur.next

        cur.next = new_node
        new_node.prev = cur

    def append_front(self, value):
        cur = self.head
        new_node = Node(value)

        cur.next = new_node
        new_node.prev = cur


    @property
    def length(self):
        i = 0
        cur = self.head

        while self.next != None:
            i += 1
            cur = cur.next

        return i

    def delete_last(self):
        second_last = self.length - 1
        i = 0

        cur = self.head

        while i != second_last:
            cur = cur.next

        cur.next = None
    
    def delete_front(self):
        cur = self.head

        cur.next = cur.next.next
        cur.next.prev = cur



    





ll = LL()

ll.append(10)
ll.append(20)

print(ll.length)

ll.print_ll()
ll.delete(1)



dll = DLL()

dll.append(10)

dll.append(20)
dll.append(30)

dll.append(40)

dll.print_dll()

dll.delete(0)
print(dll.length)

dll.delete(2)

print(dll.length)



dq = deque()


dq.append_front(10)

print(dq)
dq.append_front(20)
print(dq)
dq.append_last(30)
print(dq)
dq.delete_front()
print(dq)
dq.delete_last()


