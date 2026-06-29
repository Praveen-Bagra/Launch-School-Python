class CircularBuffer:
    def __init__(self, buffer_size):
        self._insert_index = 0
        self._buffer = []
        self._buffer_size = buffer_size
        self._oldest_index = self._calculate_oldest_index()

        self._fill_buffer()
   
    def put(self, value):
        self._buffer[self._insert_index] = value
        self._oldest_index = self._calculate_oldest_index()

        self._insert_index += 1
        if self._insert_index == self._buffer_size:
            self._insert_index = 0

    def get(self):
        _oldest_index = self._oldest_index
        _oldest_value = None
        while True:
            if self._buffer[_oldest_index] is not None:
                _oldest_value = self._buffer[_oldest_index]
                self._buffer[_oldest_index] = None
                break
            
            _oldest_index += 1
            if _oldest_index == self._buffer_size:
                _oldest_index = 0

            if _oldest_index == self._oldest_index:
                break

        return _oldest_value

    def _calculate_oldest_index(self):
        _oldest_index = self._insert_index - (self._buffer_size - 1)
        if _oldest_index < 0:
           _oldest_index = self._buffer_size - abs(_oldest_index)

        return _oldest_index
        
    def _fill_buffer(self):
        for _ in range(self._buffer_size):
            self._buffer.append(None)

    def __str__(self):
        return str(self._buffer)

buffer = CircularBuffer(3)

print(buffer.get() is None)          # True

buffer.put(1)
buffer.put(2)
print(buffer.get() == 1)             # True

buffer.put(3)
buffer.put(4)
print(buffer.get() == 2)             # True

buffer.put(5)
buffer.put(6)
buffer.put(7)
print(buffer.get() == 5)             # True
print(buffer.get() == 6)             # True
print(buffer.get() == 7)             # True
print(buffer.get() is None)          # True

buffer2 = CircularBuffer(4)

print(buffer2.get() is None)         # True

buffer2.put(1)
buffer2.put(2)
print(buffer2.get() == 1)            # True

buffer2.put(3)
buffer2.put(4)
print(buffer2.get() == 2)            # True

buffer2.put(5)
buffer2.put(6)
buffer2.put(7)
print(buffer2.get() == 4)            # True
print(buffer2.get() == 5)            # True
print(buffer2.get() == 6)            # True
print(buffer2.get() == 7)            # True
print(buffer2.get() is None)         # True

buffer2.put(1)
buffer2.put(2)
print(buffer2._buffer)