class Animal:
    def speak(self):
        return "Animal speaks"

class Bird(Animal):
    def fly(self):
        return "Bird flies"

class Fish(Animal):
    def swim(self):
        return "Fish swims"

class Duck(Bird, Fish):
    def quack(self):
        return "Duck quacks"

duck = Duck()
print(duck.speak())   # Output: Animal speaks
print(duck.fly())     # Output: Bird flies
print(duck.swim())    # Output: Fish swims
print(duck.quack())   # Output: Duck quacks