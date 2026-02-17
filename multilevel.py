class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def bark(self):
        return "Dog barks"

class Puppy(Dog):
    def weep(self):
        return "Puppy weeps"

puppy = Puppy()
print(puppy.speak())  # Output: Animal speaks
print(puppy.bark())   # Output: Dog barks
print(puppy.weep())   # Output: Puppy weeps