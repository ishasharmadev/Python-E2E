class BankAccount : 
    def __init__(self, balance) : 
        self.balance = balance

    def borrow(self, amountb) : 
        if(self.balance > amountb) : 
            self.balance -= amountb
            print(f"Your balance after withdrawing {amountb} is {self.balance}")
        else : 
            print("You don't have enough balance to withdraw")

    def deposit(self, amount) : 
        self.balance += amount
        print(f"Your balance after depositing {amount} is {self.balance}")

person = BankAccount(10000)
person.deposit(500)
person.borrow(1999)
person.borrow(3212313)
