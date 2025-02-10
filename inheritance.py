#Parent/Super/Base class

class Animal:
    def speak(self):
        print("Animal is speaking")
#Child class/sub/derived
class Dog(Animal):
    def bark(self):
        print("Dod is barking")
class Cat:
    def meow(self):
        print("The cat is meowing")

a = Animal()

d= Dog()
d.speak()

c = Cat()