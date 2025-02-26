class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight if weight > 0 else 0
        
    def eat(self):
        self.weight += 0.5
        return f"{self.name} is eating and gained some weight. Current weight = {self.weight}"
    
    def walk(self):
        return f"{self.name} is walking in garden."
    
    def make_sound(self):
        return f"{self.name} is making noise here. Something happened." 
    
    def __str__(self):
        return f"{self.name} (Age: {self.age} years old, {self.weight} kg)"
       
    
class Cow(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
    
    def make_sound(self):
        return f"{self.name} says 'Moo!'"
      
      
class Dog(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        
    def make_sound(self):
        return f"{self.name} is barking."
        
class Chicken(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        
    def make_sound(self):
        return f"{self.name} says 'baq baq baq'"
    
if __name__ == "__main__":
    bessie = Cow("Bessie", 5, 170)
    tiger = Dog("Tiger", 3, 20)
    xoroz = Chicken("Xo'roz", 2, 2)
    

    print(bessie.make_sound())
    print(tiger.make_sound())
    print(xoroz.eat())     