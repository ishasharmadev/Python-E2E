class Book : 
    def __init__(self, author, name) : 
        self.author = author
        self.name = name

    def describe(self) : 
        print(f"The book {self.name} is written by {self.author}")

book1 = Book('Sean Covey', '7 habits')
book1.describe()