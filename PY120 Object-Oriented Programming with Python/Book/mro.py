class LandDwellingMixin:
    pass

class LanguageMixin:
    pass

class BipedalismMixin:
    pass

class Creature:
    pass

class Mammal(Creature):
    def foo(self):
        pass

class Primate(LandDwellingMixin, Mammal):
    pass

class Human(Primate,
            BipedalismMixin,
            LanguageMixin):
    pass

print(Human.mro())
        