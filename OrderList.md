class OrderList:

    def __init__(self, initial_elements=[]):
        self.elements = list(initial_elements)

    def __str__(self):
        return str(self.elements)

    def __len__(self):
        return len(self.elements)

    def __getitem__(self, index):
        if index < 0 or index >= len(self.elements):
            raise IndexError("El índice no existe")
        return self.elements[index]

    def isEmpty(self):
        return len(self.elements) == 0

    def __iter__(self):
        return iter(self.elements)

    def __contains__(self, element):
        return element in self.elements

    def add(self, element):
        self.elements.append(element)

    def remove(self, element):
        if element not in self.elements:
            raise ValueError("El elemento no existe")
        self.elements.remove(element)

    def pop(self, index):
        if index < 0 or index >= len(self.elements):
            raise IndexError("El índice no existe")
        return self.elements.pop(index)

    def clear(self):
        self.elements.clear()
