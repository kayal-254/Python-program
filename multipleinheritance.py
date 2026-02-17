class Flyer:
    def fly(self):
        return "Can fly"

class jumper:
    def jump(self):
        return "Can jump"

class frog(Flyer, jumper):
    def quack(self):
        return "Frog quacks"

frog = frog()
print(frog.fly())      # Output: Can fly
print(frog.jump())     # Output: Can jump
print(frog.quack())    # Output: Frog quacks