# Not following Liskov Substitution Principle
class Bird : 
    def fly(self) : 
        pass

class Penguin(Bird) : 
    def fly(self) :
        print("I can't fly")
        # Thus not applicable


# Following LSP
class Bird :
    def move(self) :
        pass

class Penguin(Bird) : 
    def move(self) :
        print("I swim")

class Ostrich(Bird) : 
    def move(self):
        print("I run")