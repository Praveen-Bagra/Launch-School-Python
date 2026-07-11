
class Television:
    @classmethod
    def manufacturer(cls):
        return 'Amazon'

    def model(self):
        return 'Omni Fire'

tv = Television()
print(tv.manufacturer()) # Prints Amazon
print(tv.model()) # Prints Omni Fire

print(Television.manufacturer()) # Prints Amazon
print(Television.model()) # TypeError

