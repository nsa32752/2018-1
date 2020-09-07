class BankAccount:
    def __init__(self, name=0, balance = 0):
        """initalizes a BankAccount objects arguments"""
        self.__name = name
        self.balance = balance
        if balance < 0:
            self.__balance = 0
        elif balance != 0 :
            self.__balance = balance
        else:
            self.__balance = 0
        BankAccount.__no_of_accounts += 1

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

    __no_of_accounts = 0

    @staticmethod
    def count_accounts():
        return BankAccount.__no_of_accounts

print(BankAccount.count_accounts())
acct4 = BankAccount("Bbanjiri",-1000000)
print(BankAccount.count_accounts())
print(acct4.count_accounts())
#print(BankAccount.__no_of_accounts) # should produce error