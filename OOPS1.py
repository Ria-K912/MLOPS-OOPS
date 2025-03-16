class employee:
    #special method/magic method/dunder method-constructor
    def __init__(self):
        print("Started executing attributes/data")
        self.id=123
        self.salary=50000
        self.designation= "SDE"
        print("attributes/data have been initiated")
        
    def travel(self,destination):
        print("This travel method was called manually")
        print(f"Employee is travelling to {destination}")
        
sam = employee()

# print(sam.salary)
sam.travel("Bangalore")
print(type(sam))