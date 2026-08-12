class CustomSet:
    def __init__(self, lst=None):
        if lst is None:
            lst = []
        self._set_members(lst)

    def __len__(self):
        return len(self._members)

    def __iter__(self):
        # self.current = 0
        # return self

        # current = 0
        # while current < len(self):
            # yield self._members[current]
            # current += 1

        return iter(self._members)

    # def __next__(self):
        # if self.current < len(self):
            # result = self._members[self.current]
            # self.current += 1
            # return result
        # else:
            # raise StopIteration

    def __contains__(self, item):
        return item in self._members
    
    def __eq__(self, other_custom_set):
        return self.is_same(other_custom_set)

    def _set_members(self, lst):
        self._members = []
        for element in lst:
            self.add(element)

    def is_empty(self):
        return len(self) == 0

    def contains(self, element):
        return element in self

    def is_subset(self, other_custom_set):
        for member in self:
            if member not in other_custom_set:
                return False

        return True

    def is_disjoint(self, other_custom_set):
        for member in self:
            if member in other_custom_set:
                return False

        return True

    def is_same(self, other_custom_set):
        if len(self) != len(other_custom_set):
            return False

        return self.is_subset(other_custom_set)

    def add(self, member):
        if member not in self:
            self._members.append(member)

    def intersection(self, other_custom_set):
        result = CustomSet()
        for member in self:
            if member in other_custom_set:
                result.add(member)

        return result

    def difference(self, other_custom_set):
        result = CustomSet()
        for member in self:
            if member not in other_custom_set:
                result.add(member)
            
        return result

    def union(self, other_custom_set):
        result = CustomSet()

        for member in self:
            result.add(member)

        for member in other_custom_set:
            if member not in result:
                result.add(member)

        return result






    
