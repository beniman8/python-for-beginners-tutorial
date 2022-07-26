
class GreetingClass:

    name='bob'


    def say_hello(self):

        return f"Hello {self.name}"

    def say_goodbye(self):

        return f"Goodbye {self.name}"

greets = GreetingClass()


print(greets.say_hello())
print(greets.say_goodbye())