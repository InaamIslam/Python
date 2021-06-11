class Dog:
    energy = "high" #This is an attribute 

    def speak(self):   #This is a method 
        print("woof")

bilbo_waggins = Dog()
print(bilbo_waggins.energy)
bilbo_waggins.speak()

chewbarka = Dog()
chewbarka.energy = "low"
print(chewbarka.energy)
chewbarka.speak()

class Dog:
    def __init__(self, name, breed, energy):
        self.name = name
        self.breed = breed
        self.energy = energy

dog1 = Dog("Ross Barkley", "Jack Russel", "High")
print(dog1)