# Not following Open Closed Principle
class PaymentProcess : 
    def process_payment (self, mode) : 
        if mode == 'online' :
            print("Give UPI options")
        if mode == 'card' : 
            print("Give card options")


# Following OCP
class PaymentProcess :
    def process_payment (self, mode) :
        paymentProcess()
    
    def onlinePayment(self) : 
        print("Give UPI options")
    
    def cardPayment(self) : 
        print("Give card options")