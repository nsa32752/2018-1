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

# test cases
acct1 = BankAccount("Yebbuni", 100000)
print(acct1.name)
print(acct1.balance)
acct1.balance += 100000000
print(acct1.balance)
acct1.name = "Doseonsaeng"
print(acct1.name)
acct2 = BankAccount("Monnani")
print(acct2.balance)
acct3 = BankAccount("Bbanjiri", -1000000)
print(acct3.balance)