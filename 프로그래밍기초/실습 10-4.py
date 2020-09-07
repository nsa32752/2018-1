class BankAccount:
    def __init__(self, name, balance = 0):
        """initalizes a BankAccount objects arguments"""
        self.__name = name
        self.balance = balance
        if balance < 0:
            self.__balance = 0
        elif balance != 0 :
            self.__balance = balance
        else:
            self.__balance = 0

    def show_name(self):
        """returns its name value"""
        return print(self.__name)

    def show_balance(self):
        """returns its balance value"""
        if int(self.__balance) > 0:
             return print(self.__balance)
        else:
            return 0

    def deposit(self,amount):
        self.__balance += amount
        return self.__balance

    def withdraw(self,amount):
        self.__balance -= amount
        return self.__balance

acct2 = BankAccount("Gomdori", 50000)
#print(acct2.name) # should produce error
#print(acct2.__name) # should produce error
acct2.__name = 'Pooh'
acct2.show_name()
acct2.show_balance()
acct2.__balance = 100000000
acct2.show_balance()
acct2.balance = 100000000
acct2.show_balance()
acct2.deposit(20000)
acct2.show_balance()
acct2.withdraw(5000)
acct2.show_balance()