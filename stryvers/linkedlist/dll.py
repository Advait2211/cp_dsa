class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        cur = self.head

        new_node = Node(data)

        while cur.next != None:
            cur = cur.next

        new_node.prev = cur
        cur.next = new_node

    def print_dll(self):
        cur = self.head
        val = []
        cur = cur.next

        while cur:
            val.append(cur.data)
            cur = cur.next

        print(val)

    def delete(self, data):
        pass


dll = DoubleLinkedList()

dll.append(10)

dll.append(20)

dll.print_dll()




        

        