class NodeS:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class NodeD:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_in_front(self, value):
        newNode = NodeS(value)
        newNode.next = self.head
        self.head = newNode

    def insert_in_back(self, value):
        newNode = NodeS(value)
        if self.head is None:
            self.head = newNode
        else:
            p = self.head
            while p.next is not None:
                p = p.next
            p.next = newNode

    def delete_at_front(self):
        if self.head is None:
            return "Error"
        q = self.head
        self.head = self.head.next
        del q

    def delete_at_back(self):
        if self.head is None:
            return "Error"
        p = self.head
        q = None
        while p.next is not None:
            q = p
            p = p.next
        if q is None:
            del self.head
            self.head = None
        else:
            del p
            q.next = None

    def search(self, val):
        p = self.head
        index = 0
        while p is not None:
            if p.data == val:
                return index
            index += 1
            p = p.next
        return None

    def clear(self):
        self.head = None

    def size(self):
        p = self.head
        length = 0
        while p is not None:
            length += 1
            p = p.next
        return length

    def print_forward(self):
        p = self.head
        while p is not None:
            print(p.data)
            p = p.next
        return None

    def print_backward(self):
        self.backward(self.head)

    def backward(self, p):
        if p is None:
            return
        self.backward(p.next)
        print(p.data)

    def reverse_recursive(self, p=0):
        isFirst = False
        if p == 0:
            p = self.head
            isFirst = True
        if p is None:
            return None
        q = self.reverse_recursive(p.next)
        if isFirst:
            p.next = None
        if q is not None:
            q.next = p
        else:
            self.head = p
        return p

    def reverse_non_recursive(self):
        p = self.head
        while p is not None:
            pass


testS = SinglyLinkedList()
testS.insert_in_front(2)
testS.insert_in_front(1)
testS.insert_in_back(3)

print("print in forward: ")
testS.print_forward()

print("print in backward: ")
testS.print_backward()

print("search 4: ")
print(testS.search(4))

print("search 3: ")
print(testS.search(3))

print("print size: ")
print(testS.size())

print("print the reversed list in forward (recursive): ")
testS.reverse_recursive()
testS.print_forward()

print("print the reversed list in forward (non recursive): ")
testS.reverse_non_recursive()
testS.print_forward()