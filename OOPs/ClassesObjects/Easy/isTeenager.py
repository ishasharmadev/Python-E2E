class Teenager : 
    def __init__(self, age) : 
        self.age = age
    
    def isTeenager(self) : 
        if (self.age >= 13 and self.age < 20) : 
            print("You are a teenager")
        else : 
            print("You are not a teenager")

teen1 = Teenager(18)
teen1.isTeenager()

teen2 = Teenager(23)
teen2.isTeenager()