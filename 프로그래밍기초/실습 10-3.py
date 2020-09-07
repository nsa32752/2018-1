class BankAccount:
    def __init__(self, name, balance = 0):
        """initalizes a BankAccount objects arguments"""
        self.name = name
        print(name)
        if balance < 0:
            self.balance = 0
        elif balance != 0 :
            self.balance = balance
        else:
            self.balance = 0

    def show_name(self):
        """returns its name value"""
        return print(self.name)

    def show_balance(self):
        """returns its balance value"""
        if int(self.balance) > 0:
             return print(self.balance)
        else:
            return print("0")

    def deposit(self,amount):
        self.amount = amount
        if amount >= 0:
            self.balance += amount
            return self.balance
        else:
            return self.balance

    def withdraw(self,amount):
        self.amount = amount
        if amount >= 0 and self.balance >= amount:
            self.balance = self.balance - amount
            return self.balance
        else:
            return self.balance

acct1 = BankAccount("Yebbuni", 100000)
acct1.show_balance()
acct1.deposit(50000)
acct1.show_balance()
acct1.deposit(-30000)
acct1.show_balance()
acct1.withdraw(80000)
acct1.show_balance()
acct1.withdraw(-30000)
acct1.show_balance()
acct1.withdraw(100000)
acct1.show_balance()