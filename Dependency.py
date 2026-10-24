#Dependency(Uses-a)
class Payment:
    def processPayment(self, amount):
        return f"Success in processing payment of ${amount}"

class ShoppingCart:
    def checkout(self, pay: Payment, amount):
        return pay.processPayment(amount)

cart = ShoppingCart()
pay = Payment()
print(cart.checkout(pay, 20.45))