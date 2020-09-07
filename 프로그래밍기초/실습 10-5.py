class BankAccount:
    def __init__(self, name=0, balance = 0):
        """initalizes a BankAccount objects arguments"""
        self.name = name
        self.balance = balance
        print(name)
        if balance < 0:
            self.__balance = 0
        elif balance != 0 :
            self.__balance = balance
        else:
            self.__balance = 0
        BankAccount.no_of_accounts += 1

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

    no_of_accounts = 0


print(BankAccount.no_of_accounts)
acct1 = BankAccount("Yebbuni",100000)
acct1.show_balance()
print(BankAccount.no_of_accounts)
acct2 = BankAccount("Gomdori",50000)
print(BankAccount.no_of_accounts)
acct3 = BankAccount("Monnani")
print(BankAccount.no_of_accounts)
acct4 = BankAccount("Bbanjiri",-1000000)
print(BankAccount.no_of_accounts)