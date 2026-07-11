class Cat:
    def get_name(self):
        # if not hasattr(self, 'name'):
            # return 'Name not set!'

        # return self.name

        try:
            return self.name
        except AttributeError:
            return 'Name not set!'

cat1 = Cat()
print(cat1.get_name())