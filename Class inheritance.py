class Animal:
    def __init__(self):
        self.no_of_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this under water! Amazing right??")

    def swim(self):
        print("Moving in bottle of wotah")


nemo = Fish()
print(nemo.no_of_eyes)
nemo.breathe()
nemo.swim()