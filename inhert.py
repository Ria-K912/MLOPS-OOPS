
# class Animal:
#     def __init__(self,name):
#         self.name = name
#         print("Animal class constructor called")
        
#     def speak(self):
#         print(f"{self.name} is making a sound")
    
# class Dog(Animal):
#     def __init__(self): #constructor overloading
#         self.behaviour = "friendly"
#     def speak1(self):
#         print(f"{self.name} is barking. He is vert {self.behaviour}")
        

# # animal = Animal ("Generic Animal")
# # animal.speak()
# dog = Dog()
# dog.speak()

#super
class Animal:
    def __init__(self, name):
        self.name = name
        print("Animal class constructor called")
        
    def speak(self):
        print(f"{self.name} is making a sound")


class Dog(Animal):
    def __init__(self, name, breed):  # Add name parameter
        super().__init__(name)  # Pass name to Animal's constructor
        self.breed = breed
        print("Dog class constructor called")

    def speak1(self):
        super().speak()
        print(f"{self.name} is barking. He is a {self.breed}")


# Create a Dog object with both name and breed
dog = Dog("Buddy", "Golden Retriever")
dog.speak()  # This will call the speak() method from Animal class
dog.speak1()  # This will call Dog's speak1() method
