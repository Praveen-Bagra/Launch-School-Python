class SpeakMixin:
    def speak(self):
        pass

class SwimMixin(SpeakMixin):

    def swim(self):
        return 'swimming!'

class Pet:

    def speak(self):
        pass

class Mammal(Pet):

    def run(self):
        return 'running!'

    def jump(self):
        return 'jumping!'

class Fish(SwimMixin, Pet):
    pass

class Dog(SwimMixin, Pet):

    def speak(self):
        return 'bark!'

    def fetch(self):
        return 'fetching!'

class Cat(Pet):

    def speak(self):
        return 'meow!'

print(Fish.mro())