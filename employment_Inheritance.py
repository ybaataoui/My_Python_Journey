class Employees:
    def __init__(self, name, last) -> None:
        self.name = name 
        self.last = last

class Supervisors(Employees):
    def __init__(self, name, last, password):
        super().__init__(name, last)
        self.password = password

class Chefs(Employees):
    def leave_request(self, days):
        return "May I take a leave for " + str(days) + " days"
    

adrian = Supervisors("Adrian", "A", "apple")

emily = Chefs("Emily", "E")
juno = Chefs("Juno", "J")

print(emily.leave_request(3))
print(adrian.password)
print(emily.name)

print(issubclass(Supervisors, Employees)) # issubclass is a class that check if a class is a child of another class. issubclass(child, parent) should return True.
# isinstance() determines if some object is an instance of some class. 
print(isinstance(adrian, Chefs)) # return True if ogject is an instance of class.