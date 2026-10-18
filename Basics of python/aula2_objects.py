class Car:
    def __init__(self, name, hp, color, year): #__init__ is a constructor method. He is called when objecs is created.
        self.name = name # Self is a reference to the current instance of the class. 
        self.hp = hp 
        self.color = color
        self.year = year 

    def start(self):
        print(f"The {self.name} is starting")

    def check_hp(self):
        print(f"The {self.name} has {self.hp} hp")

Car1 = Car("Larborghini", 780, "orange", 2020) #Create a obejct in the class Car. The object is called Car1 and the parameters are passed to the constructor method __init__.
Car1.start() # That is te calling for use the method start in the object Car1
Car1.check_hp()