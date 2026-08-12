class Element:
    def __init__(self, datum, next_element=None):
        self._datum = datum
        self._next = next_element

    @property
    def datum(self):
        return self._datum

    @property
    def next(self):
        return self._next

    def is_tail(self):
        return self._next is None

class SimpleLinkedList:
    def __init__(self):
        self._list = []

    @property
    def size(self):
        return len(self._list) 

    def is_empty(self):
        return len(self._list) == 0

    def push(self, value):
        if self.is_empty():
            element = Element(value)
        else:
            element = Element(value, self._list[0])

        self._list.insert(0, element)

    def peek(self):
        if self.is_empty():
            return None

        return self._list[0].datum

    @property
    def head(self):
        if self.is_empty():
            return None

        return self._list[0]

    def pop(self):
        if self.is_empty():
            return None

        return self._list.pop(0).datum

    @classmethod
    def from_list(cls, iterable):
        if iterable is None:
            return cls()

        if isinstance(iterable, list):
            if not iterable:
                return cls()

            lst = cls()
            for obj in iterable[::-1]:
                lst.push(obj)
                
        return lst

    def to_list(self):
        return [element.datum for element in self._list]

    def reverse(self):
        lst = SimpleLinkedList()
        for element in self._list:
            lst.push(element.datum)

        return lst

class Element:
    def __init__(self, datum, next_element=None):
        self._datum = datum
        self._next = next_element

    @property
    def datum(self):
        return self._datum

    @property
    def next(self):
        return self._next

    def is_tail(self):
        return self._next is None

class SimpleLinkedList:
    def __init__(self):
        self._head = None

    @property
    def head(self):
        return self._head

    @property
    def size(self):
        size = 0
        current_elem = self._head
        while current_elem:
            size += 1
            current_elem = current_elem.next
        return size

    def is_empty(self):
        return self._head is None

    def push(self, datum):
        element = Element(datum, self._head)
        self._head = element

    def peek(self):
        return self._head.datum if self._head else None

    def pop(self):
        datum = self.peek()
        if self._head:
            self._head = self._head.next
        return datum

    @classmethod
    def from_list(cls, lst=None):
        if lst is None:
            lst = []

        linked_list = cls()
        for datum in reversed(lst):
            linked_list.push(datum)
        return linked_list

    def to_list(self):
        lst = []
        current_elem = self._head
        while current_elem:
            lst.append(current_elem.datum)
            current_elem = current_elem.next
        return lst

    def reverse(self):
        reversed_list = SimpleLinkedList()
        current_elem = self._head
        while current_elem:
            reversed_list.push(current_elem.datum)
            current_elem = current_elem.next
        return reversed_list

    