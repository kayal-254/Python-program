class Animal:
    def speak(self):
        return "Animal speaks"

class cat(Animal):
    def shout(self):
        return "cat shout"

cat = cat()
print(cat.speak())  
print(cat.shout())   