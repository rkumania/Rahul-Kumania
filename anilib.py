#Author: Rahul Kumania

##Looking at polymorphism and Inheritance

class Animal(): #loaded in the memory

    aCount = 0 #Our counter

    #Constructor
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        Animal.aCount += 1


    def getaCount(self):
        return Animal.aCount

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getWeight(self):
        return self.weight

    def setWeight(self, weight):
        self.weight = weight

    def speak(self):
        pass

    def __str__(self): #telling python what to print when we are printing object
        aString = "AnimalObj: " + self.name + str(self.weight)
        return aString

    def __del__(self): #Deconstructor
        print("An Animal has been destroyed: ", self.name)
        Animal.aCount -= 1


class Cat(Animal): #Inheriting from animal class

    def __init__(self, name, weight, color):
        Animal.__init__(self, name, weight)
        self.color = color

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def speak(self):
        print("Meow!")

class Dog(Animal): #Inheriting from animal class

    def __init__(self, name, weight, color):
        Animal.__init__(self, name, weight)
        self.color = color

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def speak(self):
        print("Woof!")
    




