class Greeting:
    def greet(self, message):
        print(message)

class Hello(Greeting):
    def hi(self):
        self.greet('Hello')

class Goodbye(Greeting):
    def bye(self):
        self.greet('Goodbye')
        
# hello = Hello()
# hello.hi() # Prints Hello

# hello = Hello()
# hello.bye() # AttributeError

# hello = Hello()
# hello.greet() # TypeError

# hello = Hello()
# hello.greet('Goodbye') # Prints Goodbye

# Hello.hi() # TypeError