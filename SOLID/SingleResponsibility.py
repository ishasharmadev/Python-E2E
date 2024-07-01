# Not following Single Responsibility Principle

class User : 
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def save2DB(self) : 
        print("Saving user to DB")

    def sendEmailConfirmation(self) : 
        print("Sending OTP to email")



# Following SRP
class Employee :
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def describe() : 
        print(f"Hello {self.name}! Your email ID is {self.email}")

class Save2DB :
    def save2DB(self, user) : 
        print("Saving user to DB")

class EmailConfirmation :
    def sendEmailConfirmation(self, email) :
        print("Sending OTP to email")
