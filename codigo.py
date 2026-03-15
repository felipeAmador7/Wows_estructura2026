
// Código Stack

class Stack:
    def _init_(self):
        self.items = []


    def is_empty(self):
        return len(self.items) == 0


    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            print("La pila está vacía")
            return None
        return self.items.pop()

    
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    
    def size(self):
        return len(self.items)


// Código Queque

class Queue:
    def _init_(self, initial_elements=None):
        if initial_elements is None:
            initial_elements = []
        self.elements = list(initial_elements)
    
    def _str_(self):
        return f"Queue({self.elements})"
    
    def _len_(self):
        return len(self.elements)
    
    def isEmpty(self):
        return len(self.elements) == 0
    
    def peek(self):
        if self.isEmpty():
            raise IndexError("Peek desde una cola vacía")
        return self.elements[0]
    
    def _iter_(self):
        return iter(self.elements)
    
    def _contains_(self, element):
        return element in self.elements
    
    def push(self, element):
        self.elements.append(element)
    
    def pop(self, index=0):
        if self.isEmpty():
            raise IndexError("Pop desde una cola vacía")
        return self.elements.pop(index)
    
    def clear(self):
        self.elements.clear()
    
    def extend(self, iterable):
        self.elements.extend(iterable)
    
    def copy(self):
        return Queue(self.elements.copy())
    
    def tail(self):
        if self.isEmpty():
            raise IndexError("Tail desde una cola vacía")
        return self.elements[-1]

// Código Circular List

class Node:
    def _init_(self, data):
        self.data = data
        self.next = None


class CircularList:
    def _init_(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head

    def insert(self, index, value):
        if index < 0:
            return

        new_node = Node(value)

        if index == 0:
            if self.head is None:
                self.head = self.tail = new_node
                new_node.next = self.head
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = self.head
            return

        current = self.head
        i = 0

        while i < index - 1 and current.next != self.head:
            current = current.next
            i += 1

        new_node.next = current.next
        current.next = new_node

        if current == self.tail:
            self.tail = new_node

    def delete(self, index):
        if self.head is None or index < 0:
            return

        if index == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.tail.next = self.head
            return

        current = self.head
        i = 0

        while i < index - 1 and current.next != self.head:
            current = current.next
            i += 1

        node_to_delete = current.next
        current.next = node_to_delete.next

        if node_to_delete == self.tail:
            self.tail = current

    def display(self):
        if self.head is None:
            print("Lista vacía")
            return

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break

        print("(Head)")


cl = CircularList()

cl.append("A")
cl.append("B")
cl.append("C")
cl.display()

cl.delete(0)
cl.display()

cl.insert(1, "Z")
cl.display()
