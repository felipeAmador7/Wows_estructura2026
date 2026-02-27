
class ArrayList:

    def __init__(self):
        self._data = []
        self._size = 0

    def size(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    
    def add(self, *args):

        
        if len(args) == 1:
            element = args[0]
            self._data.append(element)
            self._size += 1

        
        elif len(args) == 2:
            index, element = args

            if index < 0 or index > self._size:
                raise IndexError("Índice fuera de rango")

            self._data.append(None)

            for i in range(self._size, index, -1):
                self._data[i] = self._data[i - 1]

            self._data[index] = element
            self._size += 1

        else:
            raise TypeError("Número incorrecto de argumentos")

    
    def remove(self, index):

        if index < 0 or index >= self._size:
            raise IndexError("Índice fuera de rango")

        removed = self._data[index]

        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]

        self._data.pop()
        self._size -= 1

        return removed

    
    def get(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Índice fuera de rango")
        return self._data[index]

    def set(self, index, element):
        if index < 0 or index >= self._size:
            raise IndexError("Índice fuera de rango")
        self._data[index] = element

    def contains(self, element):
        for i in range(self._size):
            if self._data[i] == element:
                return True
        return False

    def clear(self):
        self._data = []
        self._size = 0



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self._size = 0

    def size(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    
    def addFirst(self, element):
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def addLast(self, element):
        new_node = Node(element)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

        self._size += 1

    def add(self, index, element):

        if index < 0 or index > self._size:
            raise IndexError("Índice fuera de rango")

        if index == 0:
            self.addFirst(element)
            return

        new_node = Node(element)
        current = self.head

        for _ in range(index - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self._size += 1

    
    def removeFirst(self):
        if self.isEmpty():
            raise IndexError("Lista vacía")

        removed = self.head.data
        self.head = self.head.next
        self._size -= 1
        return removed

    def removeLast(self):
        if self.isEmpty():
            raise IndexError("Lista vacía")

        if self._size == 1:
            return self.removeFirst()

        current = self.head
        while current.next.next:
            current = current.next

        removed = current.next.data
        current.next = None
        self._size -= 1
        return removed

    def remove(self, index):

        if index < 0 or index >= self._size:
            raise IndexError("Índice fuera de rango")

        if index == 0:
            return self.removeFirst()

        current = self.head
        for _ in range(index - 1):
            current = current.next

        removed = current.next.data
        current.next = current.next.next
        self._size -= 1
        return removed

    
    def get(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Índice fuera de rango")

        current = self.head
        for _ in range(index):
            current = current.next

        return current.data

    def set(self, index, element):
        if index < 0 or index >= self._size:
            raise IndexError("Índice fuera de rango")

        current = self.head
        for _ in range(index):
            current = current.next

        current.data = element

    def contains(self, element):
        current = self.head
        while current:
            if current.data == element:
                return True
            current = current.next
        return False

    def clear(self):
        self.head = None
        self._size = 0




if __name__ == "__main__":

    print("PRUEBA ARRAYLIST")
    arr = ArrayList()
    arr.add(10)
    arr.add(20)
    arr.add(1, 99)
    print("Elemento en índice 1:", arr.get(1))
    print("Contiene 20:", arr.contains(20))
    print("Eliminado:", arr.remove(1))
    print("Tamaño:", arr.size())

    print("\nPRUEBA LINKEDLIST")
    lst = LinkedList()
    lst.addFirst(5)
    lst.addLast(15)
    lst.add(1, 10)
    print("Elemento en índice 1:", lst.get(1))
    print("Contiene 15:", lst.contains(15))
    print("Eliminado:", lst.remove(100))
    print("Tamaño:", lst.size())
