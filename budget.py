class Budget:
    def __init__(self):
        self.balance = 0


    def withdraw(self,amount):
        if self.balance == 0:
            print("Insufficient balance. Unable to complete request.")

        elif amount > self.balance:
            print("Insufficient balance. Unable to complete request.")
        else:
            self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def makeTransfer(self, amount):
         self.withdraw(amount)
         return amount

    def acceptTransfer(self, amount):
        self.balance += amount