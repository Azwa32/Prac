"""
Create a class hierarchy to represent different types of animals. 
The base class should be Animal, which has the following attributes:

name: A string representing the animal's name
age: An integer representing the animal's age in years
gender: A string representing the animal's gender ('male', 'female', or 'unknown')
The Animal class should also have the following methods:

speak(): Prints a string representing the sound the animal makes
move(): Prints a string representing how the animal moves
Create two subclasses of Animal: Mammal and Bird. 
The Mammal class should have an additional attribute fur_color, 
while the Bird class should have an additional attribute wing_span. 
Both Mammal and Bird should override the speak() and move() methods with their own implementations.

Create two subclasses of Mammal: Dog and Cat. 
The Dog class should have an additional attribute breed, 
while the Cat class should have an additional attribute eye_color. 
Both Dog and Cat should override the speak() and move() methods with their own implementations.

Create two subclasses of Bird: Eagle and Penguin. 
The Eagle class should have an additional attribute flight_speed, 
while the Penguin class should have an additional attribute swimming_speed. 
Both Eagle and Penguin should override the speak() 
and move() methods with their own implementations.

Create instances of each class and call their methods to verify that they work correctly.
"""

class Animal:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self):
        print("a sound")

    def move(self):
        print("a move")

class Mammal(Animal):
    def __init__(self, name, age, gender, fur_color):
        super().__init__(name, age, gender)
        self.fur_color = fur_color

    def speak(self):
        print("mammal sound")

    def move(self):
        print("mammal move")

class Bird(Animal):
    def __init__(self, name, age, gender, wing_span):
        super().__init__(name, age, gender)
        self.wing_span = wing_span

    def speak(self):
        print("bird sound")

    def move(self):
        print("bird move")

class Dog(Mammal):
    def __init__(self, name, age, gender, fur_color, breed):
        super().__init__(name, age, gender, fur_color)
        self.breed = breed

    def speak(self):
        print("Woof")

    def move(self):
        print("running")

class Cat(Mammal):
    def __init__(self, name, age, gender, fur_color, eye_color):
        super().__init__(name, age, gender, fur_color)
        self.eye_color = eye_color

    def speak(self):
        print("Meow")

    def move(self):
        print("running")

class Eagle(Bird):
    def __init__(self, name, age, gender, wing_span, flight_speed):
        super().__init__(name, age, gender, wing_span)
        self.flight_speed = flight_speed

    def speak(self):
        print("Squak")

    def move(self):
        print("fly")

class Penguin(Bird):
    def __init__(self, name, age, gender, wing_span, swimming_speed):
        super().__init__(name, age, gender, wing_span)
        self.swimming_speed = swimming_speed

    def speak(self):
        print("Honk")

    def move(self):
        print("Waddle")

dog_1 = Dog("Fido", 3, "boy", "brown", "Labrador")
cat_1 = Cat("Winter", 7, "girl", "white", "green")
eagle_1 = Eagle("Biggy", 2, "boy", 34, 56)
penguin_1 = Penguin("flappy", 5, "girl", 24, 40)

print(f"{dog_1.name} {dog_1.age} {dog_1.gender} {dog_1.fur_color} {dog_1.breed}")
print(f"{cat_1.name} {cat_1.age} {cat_1.gender} {cat_1.fur_color} {cat_1.eye_color}")
print(f"{eagle_1.name} {eagle_1.age} {eagle_1.gender} {eagle_1.wing_span} {eagle_1.flight_speed}")
print(f"{penguin_1.name} {penguin_1.age} {penguin_1.gender} {penguin_1.wing_span} {penguin_1.swimming_speed}")
