import random

class Oracle:
    def predict_the_future(self):
        return f'You will {random.choice(self.choices())}.'

    def choices(self):
        return [
            'eat a nice lunch',
            'take a nap soon',
            'stay at work late',
            'adopt a cat',
        ]

oracle = Oracle()
print(oracle.predict_the_future())

# It will print "You will {any choice from self.choices dictionary}"
# Because predict_the_future() on Oracle class instance will return the
# string i.e "You will {any one value from self.choices list} "
# self.choices is an instance method that returs list. And we are passing
# this list as an argument to random.choice function which returns any one
# obj from the list on random basis.