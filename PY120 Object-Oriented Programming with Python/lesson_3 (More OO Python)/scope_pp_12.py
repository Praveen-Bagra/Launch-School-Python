class Cat:
    sound = "meow"

    @classmethod
    def make_sound(cls):
        return cls.sound

class Lion(Cat):
    sound = "roar"

print(Lion.make_sound()) 
# Prints roar because we have overwritten class variable 'sound' in class
# Lion and cls in method 'Cat.make_sound' refers to class of calling class.
# Thought it may be defined in Cat class.