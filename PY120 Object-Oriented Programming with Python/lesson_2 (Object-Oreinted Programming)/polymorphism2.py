class Wedding:

    def prepare(self, preparers):
        for preparer in preparers:
            if isinstance(preparer, Chef):
                preparer.prepare_food(guests)
            elif isinstance(preparer, Decorator):
                preparer.decorate_place(flowers)
            elif isinstance(preparer, Musician):
                preparer.prepare_performance(songs)

class Chef:

    def prepare_food(self, guests):
        # implementation goes here

class Decorator:

    def decorate_place(self, flowers):
        # implementation goes here

class Musician:

    def prepare_performance(self, songs):
        # implementation goes here

