class GoodCat:

    counter = 0         # class variable

    def __init__(self):
        GoodCat.counter += 1

    @classmethod
    def number_of_cats(cls):
        return GoodCat.counter

class ReallyGoodCat(GoodCat):
    pass

cat1 = GoodCat()
cat2 = GoodCat()
car3 = ReallyGoodCat()
cat4 = ReallyGoodCat()

print(GoodCat.number_of_cats())
print(GoodCat.counter)
print(ReallyGoodCat.number_of_cats())
print(ReallyGoodCat.counter)