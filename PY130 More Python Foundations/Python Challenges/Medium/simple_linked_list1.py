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
        return self.next is None

class SimpleLinkedList:
    def __init__(self):
        self._head = None

    @property
    def head(self):
        return self._head

    @property
    def size(self):
        size = 0
        current_element = self.head

        while current_element:
            size += 1
            current_element = current_element.next

        return size

    def is_empty(self):
        return self.head is None

    def push(self, datum):
        element = Element(datum, self.head)
        self._head = element

    def peek(self):
        return self.head.datum if self.head else None
        
    def pop(self):
        value = self.peek()
        self._head = self._head.next

        return value

    @classmethod
    def from_list(cls, input_lst=None):
        if input_lst is None:
            input_lst = []
        
        lst = SimpleLinkedList()
        for datum in reversed(input_lst):
            lst.push(datum)

        return lst

    def to_list(self):
        lst = []
        current_element = self.head

        while current_element:
            lst.append(current_element.datum)
            current_element = current_element.next

        return lst

    def reverse(self):
        # lst = list(reversed(self.to_list()))
        # return SimpleLinkedList.from_list(lst)
        reversed_list = SimpleLinkedList()
        current_element = self.head
        while current_element:
            reversed_list.push(current_element.datum)
            current_element = current_element.next

        return reversed_list