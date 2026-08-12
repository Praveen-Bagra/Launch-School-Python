class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        current = self.start
        while current > 0:
            yield current
            current -= 1

counter = Countdown(3).__iter__()
print(counter)

for num in counter:
    print(num)

for num in counter:
    print(counter)