class BankAccount:
    def __init__(self, name, balance = 0):
        """initalizes a BankAccount objects arguments"""
        self.name = name
        if balance < 0:
            self.balance = 0
        elif balance != 0 :
            self.balance = balance
        else:
            self.balance = 0


    def __str__(self):
        """returns its string representation"""
        if self.name:
            return self.name + "'s BankAccount object"

# test cases
acct1 = BankAccount("Yebbuni", 100000)
print(acct1)
acct2 = BankAccount("Monnani")
print(acct2)
acct3 = BankAccount("Bbanjiri", -1000000)
print(acct3)