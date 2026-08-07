class CreditCard:
    def pay(self, amount):
        print("Paid", amount, "using Credit Card")

class UPI:
    def pay(self, amount):
        print("Paid", amount, "using UPI")

class PayPal:
    def pay(self, amount):
        print("Paid", amount, "using PayPal")

class Payment:
    def __init__(self, method):
        self.method = method

    def process(self, amount):
        self.method.pay(amount)

payment = Payment(CreditCard())
payment.process(1000)

payment = Payment(UPI())
payment.process(500)

payment = Payment(PayPal())
payment.process(1500)