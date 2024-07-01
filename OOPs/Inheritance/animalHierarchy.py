class Animal : 
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sounds(self) : 
        pass

    def move(self) : 
        pass

    def describe(self) : 
        print(f'Hello this is {self.name} and he is {self.age} years old!')

class Dog (Animal) : 
    def sounds(self) : 
        print("Bark")

    def move(self) : 
        print("Walk")

class Bird (Animal) : 
    def sounds(self):
        print("Tweet")

    def move(self):
        print("Fly")


dog1 = Dog('Tommy', '10')
dog1.describe()
dog1.sounds()
dog1.move()